from pysysml2.modeling.model import Model as Model
from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, PostOrderIter

from pathlib import Path

def main():
    # load model
    model = Model().from_sysml2_file("model/drone_delivery_service.sysml")

    print(RenderTree(model, style=AsciiStyle()))

    for pre, fill, node in RenderTree(model):
        if isinstance(node, Model):
            continue
        print("{}".format(node.name))

    for node in PreOrderIter(model):
        if isinstance(node, Model):
            continue
        print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

    for node in PostOrderIter(model):
        if isinstance(node, Model):
            continue
        print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

if __name__ == "__main__":
    main()
