__author__ = 'lskrinjar'

import sys
import os
from pprint import pprint
import itertools
import logging
import numpy as np
import ctypes
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GL.ARB.vertex_buffer_object import *
from OpenGL.GL.shaders import *
from OpenGL.GLU import *



class Marker(object):
    '''
    classdocs
    '''
    __id = itertools.count(-1)

    def __init__(self, node, visible = True, scale = 2E-3, parent=None):
        '''
        Class constructor of VBO marker
        :param node:
        '''
        self._parent = parent
        self._visible = visible
        self._VBO_created = False
        self.scale = scale

        self.node = node

        #   create colors array - color vector for every vertex
        self._colors()



        axis = self._geometry(node)
        #   number of elements - nodes axis attribute
        self.N_axis = len(axis)


        #   flatten vbo array
        _vbo_array = np.hstack((axis, self.colors)).flatten()

        #   vbo array to use with opengl library
        self.vbo_array = np.array(_vbo_array, dtype='float32')


    def _geometry(self, node):
        #    points
        self.x_axis = self.scale*(np.array([1, 0, 0])) + node
        self.y_axis = self.scale*(np.array([0, 1, 0])) + node
        self.z_axis = self.scale*(np.array([0, 0, 1])) + node

        #   axis vector for every axes
        _x_axis = np.array([node, self.x_axis, node])
        _y_axis = np.array([node, self.y_axis, node])
        _z_axis = np.array([node, self.z_axis, node])


        #   axis matrix
        axis = np.vstack((_x_axis, _y_axis, _z_axis))
        return axis


    def _show(self):
        """

        """
        if self._visible:
            self._visible = False
        else:
            self._visible = True
        
        
    def _colors(self):
        """

        """
        #    colors
        #    red
        self.x_color = np.array([[1, 0, 0]])
        #    green
        self.y_color = np.array([[0, 1, 0]])
        #    blue
        self.z_color = np.array([[0, 0, 1]])


        #   colors vector for ewery node
        x_colors = np.repeat(self.x_color, repeats=3, axis=0)
        y_colors = np.repeat(self.y_color, repeats=3, axis=0)
        z_colors = np.repeat(self.z_color, repeats=3, axis=0)

        #   colors matrix
        self.colors = np.vstack((x_colors, y_colors, z_colors))


        
    def _create_VBO(self):
        """
        Function creates VBO of coordinate system
        """
        self.__v_pointer = ctypes.c_void_p(0)
        self.__c_pointer = ctypes.c_void_p(12)
        
        #    generate a new VBO and get the associated vbo_id
        num_of_VBOs = 1
        
        
        #    create buffer name
        self.vbo_id = GLuint()
        self.vbo_id = glGenBuffers(num_of_VBOs)
        
        #    bind name to buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_id)
        
        
        #    VBO_data size in bytes
        self.VBO_data_size_in_bytes = arrays.ArrayDatatype.arrayByteCount(self.vbo_array)
        
        
        #    allocate space and upload the data from CPU to GPU
        #    bind data to buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_id)
        
        
        #    add VBO data to buffer
        glBufferData(GL_ARRAY_BUFFER, self.VBO_data_size_in_bytes, self.vbo_array, GL_DYNAMIC_DRAW)
        self._VBO_created = True


    def _paintGL_VBO(self):
        """
        Paint local coordinate system VBO
        """
        if self._visible and self._VBO_created:

            #   bind buffer to id
            glBindBuffer(GL_ARRAY_BUFFER, self.vbo_id)
            
            #    stride in bits (1 float = 4 bits)
            stride_in_bits = 24
            
            #   pointers
            glVertexPointer(3, GL_FLOAT, stride_in_bits, self.__v_pointer)
            glColorPointer(3, GL_FLOAT, stride_in_bits, self.__c_pointer)
            glDisable(GL_LIGHTING)
    
            
            #   draw lines - opengl
#             print glGetError()
#             GLerror
#             print glGetString(GLerror)
#             print GL_NO_ERROR

            glDrawArrays(GL_LINES, 0, self.N_axis)
    
            glEnable(GL_LIGHTING)
            
            glBindBuffer(GL_ARRAY_BUFFER, 0)



    def _update_node(self, node):
        """
        Function update position of marker VBO data
        :param node:
        :return:
        """
        axis = self._geometry(node)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo_id)

        #   offset in bits
        for i in xrange(0, self.N_axis):
            vertex = axis[i].astype("float32")
            _size = arrays.ArrayDatatype.arrayByteCount(vertex)

            glBufferSubData(GL_ARRAY_BUFFER, i*24, _size, vertex)

        glBindBuffer(GL_ARRAY_BUFFER, 0)