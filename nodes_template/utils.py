from node.models import Node


def get_nodes_by_nodestemplate(nodestemplate):
    r = nodestemplate.nodeids.all()
    return r


