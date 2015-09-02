'''
Created on 21. feb. 2014

@author: lskrinjar
'''
import logging
import itertools
import time
from operator import attrgetter
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt

from ..contact.distance.distance import Distance
from MBD_system.force.force import Force
from ..q2R_i import q2R_i
from ..q2theta_i import q2theta_i
from ..q2dR_i import q2dR_i
from ..q2dtheta_i import q2dtheta_i
from ..q2q_body import q2q_body
from ..transform_cs import cm_lcs2gcs, gcs2cm_lcs
from ..dr_contact_point_uP import dr_contact_point_uP
from MBD_system.contact_model.contact_model import ContactModel
from MBD_system.contact.contact import Contact
from ..A import A_matrix
from ..Ai_ui_P import Ai_ui_P_vector
from simulation_control_widget.opengl_widget.marker.marker import Marker


class RevoluteClearanceJoint(Contact):
    '''
    classdocs
    '''
#     __id = itertools.count(0)
    def __init__(self, body_id_i, body_id_j, u_iP, u_jP, R_i, R_j, _type, properties_dict=[], parent=None):
        #    number
#         self.contact_id = self.__id.next()
        #    name as string
        self._name = "RC_Joint_"# + str(self.contact_id)

        #    this has to be after attributes contact_id and _name as name is constructed from contact_id and _name
        super(RevoluteClearanceJoint, self).__init__(body_id_i, body_id_j, _type, name=self._name, properties_dict=properties_dict, parent=parent)
        '''
        Constructor of class contact
        in:
            joint_name - string
            body_i - 
            body_j - 
        '''
        self._parent = parent

        #    joint type
        self._type = "Revolute Clearance Joint"


        #   vector of axis on revolute joint in LCS of a body i, j
        self.u_iP = u_iP
        self.u_jP = u_jP
        #   predefined empty list of center point or clearance joint (to center of pin/hole) in body LCS
        self.u_CP_list_LCS = [self.u_iP, self.u_jP]
        #   centers of revolute clearance joint in GCS
        self.u_CP_list_GCS = []
        #   predefined empty list of contact point in body LCS
        self.u_P_list_LCS = []

        #   contact point in GCS
        self.u_P_GCS = None


        #   clearance parameters
        self.R_i = R_i
        self.R_j = R_j
        self.R_list = [R_i, R_j]
        #   radial clearance
        self._radial_clearance = abs(R_i - R_j)


        #   contact model
#         self.contact_model_type = "hertz"
#         self.contact_model = ContactModel(self.contact_model_type, parent=self)


        #    joint body ids
        self.body_id_i = body_id_i
        self.body_id_j = body_id_j
        self.body_id_list = [self.body_id_i, self.body_id_j]


        for _body_id, _u_P in zip(self.body_id_list, self.u_CP_list_LCS):
            _node = np.array(np.append(_u_P, self.z_dim), dtype='float32')
            _marker = Marker(_node, visible=False)
            self._parent._parent.bodies[_body_id].markers.append(_marker)
            self.markers.append(_marker)


    def check_for_contact(self, q):
        """
        Function check for contact of revolute clearance joint
        """
        # print "check_for_contact()"
        #   evaluated distance, deltas
        self._distance, self._delta = self._contact_geometry_GCS(q)


        #   add distance value to container
        self._distance_solution_container = np.append(self._distance_solution_container, self._delta)


        #   check sign
        self._sign_check = np.sign(self._distance_solution_container[-1]*self._distance_solution_container[-2])

        
        #    contact has happened, but time step has to be reduced as initial penetration depth is too large
        # if (np.sign(self._dqn_solution_container[-1]) == +1) or (self._dqn_solution_container[-1] == 0) and (self._sign_check == -1) and (self._distance >= self._radial_clearance):
        if (self._sign_check == -1) and (self._distance >= self._radial_clearance):

            #    beginning of contact detected, all parameters are within limits
            if abs(self._delta) <= self.distance_TOL:
            # else:
            #     print "contact"
                self.contact_detected = True
                self.contact_distance_inside_tolerance = True
                self.status = 1
                # print int(self._step_num_solution_container[-1]), self.status, t, self._distance,
                return 1

            #   step back
            if abs(self._delta) > self.distance_TOL:
                # print "step back"
                self.contact_detected = True
                self.status = -1
                self._distance_solution_container = np.delete(self._distance_solution_container, -1)
                return -1

        #    all calculated distances are greater than tolerance and bodies are not in contact
        self.status = 0
        self._status_container = np.append(self._status_container, self.status)
        self.no_contact()

        for _force_n, _force_t in zip(self._Fn_list, self._Ft_list):
            _force_n.update(self._step)
            _force_t.update(self._step)

        return 0


    def _get_contact_geometry_data(self, t, q, bodies):
        """
        Function calculates a vector - point of contact from global coordinates to local coordinates of each body
        """
        #   tangent is calculated from rotation of normal for 90deg in CCW direction
        self._t = np.dot(A_matrix(np.pi/2), self._n)
        self._t_list = [self._t, -self._t]


    def _contact_geometry_CP_GCS(self, q):
        """
        Function calculates a centers of revolute joint pin/hole in GCS
        :param q:
        :return u_CP_list_GCS: a list of two arrays (vectors) of 
        """
        #   calculate position of pin/hole centers of each body in GCS
        u_CP_list_GCS = []
        for body_id, u_P in zip(self.body_id_list, self.u_CP_list_LCS):
            #   q of a body
            q_body = q2q_body(q, body_id)

            #   axis center of revolute joint of each body in GCS
            u_P_GCS = cm_lcs2gcs(u_P, q_body[0:2], q_body[2])

            u_CP_list_GCS.append(u_P_GCS)

        #   reformat to 32bit float to display in opengl scene
        return np.array(u_CP_list_GCS, dtype="float32")


    def _contact_geometry_GCS(self, q):
        """
        Function calculates
        :param q:
        :return distance_obj:   distance object of calculated data in GCS
        """
        self.u_CP_list_GCS = self._contact_geometry_CP_GCS(q)

        #   calculate distance between axis of both bodies in revolute joint
        _distance = Distance(self.u_CP_list_GCS[0], self.u_CP_list_GCS[1], parent=self)._distance

        #   penetration depth is difference between nominal radial clearance and actual calculated clearance at time t
        _delta = self._radial_clearance - _distance


        #   contact is present and actual contact point has to be evaluated
        # if _distance >= self._radial_clearance and abs(_delta) >= self.distance_TOL:
        # print "contact is present"
        #   unit vector in direction from one center to enother (pin to hole)
        self._n = (self.u_CP_list_GCS[1] - self.u_CP_list_GCS[0])/_distance
        print "--------------------------------"
        print "step =", self._step
        print "n =", self._n
        # if _delta < 0 and abs(_delta) > self.distance_TOL:
        #     print "body i =", self.u_CP_list_GCS[0]
        #     print "body j =", self.u_CP_list_GCS[1]
        #     print "n =", self._n



        #   create normal list
        self._n_list = [self._n, -self._n]


        #   calculate a actual contact point in revolute clearance joint of each body in GCS
        #   and vector of contact point in LCS
        self.u_P_list = []
        self.u_P_list_LCS = []
        plot = False#[False, self.status==2] #False
        if plot:
            print "*************************"
            fig = plt.gcf()
            plt.xlim([0.0, 0.01])
            plt.ylim([0.0, 0.01])
            ax = plt.gca()
            # ax.relim()
            ax.autoscale_view(True,True,True)
            ax.set_aspect('equal')


        self.u_P_list_LCS = []
        #   evaluate actual contact point in LCS of each body and in GCS
        for body_id, _u_CP_GCS, _u_CP_LCS, _R in zip(self.body_id_list, self.u_CP_list_GCS, self.u_CP_list_LCS, self.R_list):
            #   q of a body
            q_body = q2q_body(q, body_id)

            #   contact point in GCS
            _u_P_GCS = _u_CP_GCS + _R * self._n

            #   contact point in body LCS
            _u_P_LCS = gcs2cm_lcs(_u_P_GCS, q_body[0:2], q_body[2])
            self.u_P_list_LCS.append(_u_P_LCS)


            if plot:
                print "----------------------------------"
                print "body =", self._parent._parent.bodies[body_id]._name

                R = q_body[0:2]
                print "q_body[0:2] =", q_body[0:2]
                print "joint center =", _u_CP_LCS
                print "contact point GCS =", _u_P_GCS
                print "contact point LCS =", _u_P_LCS
                _color = np.random.rand(3)
                circle=plt.Circle((_u_CP_LCS[0]+R[0],_u_CP_LCS[1]+R[1]),_R,color=_color, fill=False)
                #   center of axis
                ax.plot(_u_CP_LCS[0], _u_CP_LCS[1], "o", color=_color)
                #   contact point
                ax.plot(_u_P_LCS[0]+R[0], _u_P_LCS[1]+R[1], "x", color=_color)
                #   LCS
                ax.plot(R[0], R[1], "s", color=_color)
                fig.gca().add_artist(circle)


        #   transform to 32bit float to display in opengl
        self.u_P_list = np.array(self.u_P_list, dtype="float32")
        self.u_P_list_LCS = np.array(self.u_P_list_LCS, dtype="float32")
        self.u_P_GCS = np.array(_u_P_GCS, dtype="float32")


        if self._step_solution_accepted:
            self._u_P_solution_container.append(self.u_P_list_LCS.flatten())

        if plot:
            plt.grid()
            plt.show()
            fig.savefig('testing.png')

        return _distance, _delta


    def contact_update(self, step, t, q):
        """
        Function evaluates contact distance while, contact is present
        :return:
            status - status of contact 0-no contact, 2-contact
        """
        self._step = step

        #   current contact velocity at time t
        self._dq_n, self._dq_t = self._contact_velocity(q)

        #   calculate distance between joint centers and delta (penetration)
        self._distance, self._delta = self._contact_geometry_GCS(q)


        #   if distance is greater than radial clearance, contact is present
        if self._distance >= self._radial_clearance and abs(self._delta) >= self.distance_TOL:
            self.status = 1

        else:
            self.status = 0
            self.contact_detected = False 
            self.contact_distance_inside_tolerance = False
            # self.list_of_contact_force_objects_constructed = False
            self._contact_point_found = False
            self.initial_contact_velocity_calculated = False


            for _force_n, _force_t in zip(self._Fn_list, self._Ft_list):
                _force_n.update(self._step)
                _force_t.update(self._step)

        return self.status


    def _contact_velocity(self, q):
        """
        Function evaluates relative contact velocity at contact point in revolute clearance joint.
        :param q:   array of coordinates (r, theta) and velocities (dR, dhete=omega) of MBD system
        """
        dr_P = []
        for body_id, u_P in zip(self.body_id_list, self.u_P_list_LCS):
            dR = q2dR_i(q, body_id)
            theta = q2theta_i(q, body_id)
            #    dtheta - omega
            dtheta = q2dtheta_i(q, body_id)

            #    point velocity
            dr_P_body = dr_contact_point_uP(dR, theta, dtheta, u_P)

            #    add to list
            dr_P.append(dr_P_body)

        _dq = dr_P[1] - dr_P[0]


        #   relative contact velocity
        #   normal direction
        _dq_n = np.dot(_dq, self._n)

        #   tangent direction
        _dq_t = np.dot(_dq, self._t)

        return _dq_n, _dq_t


if __name__ == "__main__":
    a = RevoluteClearanceJoint(body_id_i=0, body_id_j=1, u_iP=np.array([0, 0]), u_jP=np.array([-1, 0]), type="rcj", properties_dict=[], parent=None)
    print "a =", a
    pprint(vars(a))