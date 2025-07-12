from pysysml2.modeling.model import Model as Model
from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, PostOrderIter

def main():
    # Load model
    model = Model().from_sysml2_file("model/structure.sysml")
    tree = RenderTree(model)

    print(RenderTree(model, style=AsciiStyle()))

    for pre, fill, node in tree:
        if type(node) is not Model:
            print("{}".format(node.name))

    for node in PreOrderIter(model):
        if type(node) is not Model:
            print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

    for node in PostOrderIter(model):
        if type(node) is not Model:
            print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

if __name__ == "__main__":
    main()
