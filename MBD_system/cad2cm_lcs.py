"""
Created on 7. apr. 2014

@author: lskrinjar (email: skrinjar.luka@gmail.com)
"""


def cad2cm_lcs(vector_in_CAD_CS, CM_CAD_LCS):
    """
    Function transforms vector from cad-LCS to center of mass CM-LCS of a body
    :param vector_in_CAD_LCS:   vector (numpy array, [x, y]) in CAD CS of a body
    :param CM_CAD_LCS:          vector (numpy array, [x, y, z]) of center of mass in CAD CS
    :return vector_in_CM_LCS:   vector (numpy array, [x, y]) in CM LCS of a body
    """
    if len(CM_CAD_LCS) == 3:
        CM_CAD_LCS = CM_CAD_LCS[0:2]

    vector_in_CM_LCS = vector_in_CAD_CS - CM_CAD_LCS
    return vector_in_CM_LCS