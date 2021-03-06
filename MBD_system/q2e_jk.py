# coding=utf-8
"""
Created on 06. mar. 2017

@author: skrinjar.luka@gmail.com
"""

import numpy as np


from q2qdq_i import q2qdq_i


def q2e_jk(q, body_id, node_id, node_dim=4):
    """
    Function returns gradient vector of j-th node defined by node_id of k-th flexible body with id as body_id
    :param q:
    :param body_id:
    :param node_id:
    :return:
    """
    q_j, dq_j = q2qdq_i(q, body_id)

    e_x_jk = q_j[(node_dim * node_id):(node_dim * node_id) + 2]

    return e_x_jk


if __name__ == "__main__":
    q = np.arange(0, 16, 1)
    print q

    ids = [0, 1, 2, 3]

    node_dim = 4

    for _id in ids:
        print q[node_dim * _id:(node_dim * _id) + 2]