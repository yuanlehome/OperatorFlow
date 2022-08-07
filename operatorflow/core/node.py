# -*- coding: utf-8 -*-
"""
Created on 19:42, 2022/8/7

@author: liuyuanle
"""

import abc
import numpy
import operatorflow.core.graph as graph

class Node:
    """
    base class of computational graph node.
    """
    def __init__(self, *parents, **kargs):
        self.kargs = kargs
        self.graph = kargs.get('graph', graph.default_graph)
        self.need_save = kargs.get('need_save', True)
        # list of parent node
        self.parents = list(parents)
        # list of child node
        self.childs = []
        # value of node
        self.value = None
        # jacobian matrix of the result node to the current node
        self.jacobian = None
        # add the node to the list of child node of its parent nodes
        for parent in self.parents:
            parent.children.append(self)
        # add the node to the computational graph
        self.graph.add_node(self)

    def clear_jacobian(self):
        """
        clear jacobian matrix of node
        :return: none
        """
        self.jacobian = None

    def reset_value(self, recursive=True):
        """
        reset node value and recursive to its child nodes.
        :param recursive: True or False
        :return: none
        """
        self.value = None
        if recursive:
            for child in self.childs:
                child.reset_value()

    def shape(self):
        """
        return shape of node value', the value is a numpy matrix.
        :return: (rows, columns)
        """
        return self.value.shape

    def dimension(self):
        """
        return demensions of flattened node value matrix
        :return:
        """
        return self.value.shape[0] * self.value.shape[1]

    def get_parents(self):
        """
        return parents of node
        :return: list
        """
        return self.parents

    def get_childs(self):
        """
        return childs of node
        :return: list
        """
        return self.childs

    @abc.abstractmethod
    def compute(self):
        """
        compute node value according to its parents value
        :return:
        """

    def forward(self):
        """
        :return: none
        """
        for node in self.parents:
            if node.value is None:
                node.forward()

        self.compute()

    @abc.abstractmethod
    def get_jacobian(self, parent):
        """
        compute jacobian matrix of the node according to one of its parents
        :param parent:
        :return: jacobian maxtrix
        """

    def backward(self):
        """

        :return:
        """















