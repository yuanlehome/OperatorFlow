# -*- coding: utf-8 -*-
"""
Created on 19:41, 2022/8/7

@author: liuyuanle
"""

class Graph:
    """
    计算图类
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        """
        add node
        :param node: Node object
        :return: none
        """
        self.nodes.append(node)

    def clear_jacobian(self):
        """
        clear the jacobian matrix of all nodes in computational graph
        :return: none
        """
        for node in self.nodes:
            node.clear_jacobian()

    def reset_value(self):
        """
        reset value of all nodes in computational graph
        :return: none
        """
        for node in self.nodes:
            # no recursive
            node.reset_value(False)

    def node_count(self):
        """
        counts of computational graph
        :return: none
        """
        return len(self.nodes)

# global default computational graph
default_graph = Graph()