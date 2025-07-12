from json import load
from sysml2py import Model, Package, Part, load_grammar, load
from sysml2py.formatting import classtree
from sysml2py import Part

from pysysml2.modeling.model import Model as PySysML2Model
from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, PostOrderIter

def get_all_parts(model):
    """
    Recursively traverse the model and return all Part objects.

    :param model: The root model object to start traversal from.
    :return: A list of all Part objects found in the model.
    """
    parts = []

    def traverse(node):
        # Check if the current node is a Part
        if isinstance(node, Part):
            parts.append(node)

        # Recursively traverse all children of the current node
        for child in node._children:
            traverse(child)

    # Start traversal from the root of the model
    traverse(model)

    return parts

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

def get_element_by_name(model, name):
    for element in model.values():
        if isinstance(element, dict):
            yield from NestedDictValues(element)
        else:
            yield element

def main():
    text = """package ROOT {
        package Types {
        }
        package Structure {
            part drone : BatteryPoweredDevice {
            }
            part warehouse {
                part deliveryPackages;
            }
        }
    }
"""
    with open('model/types.sysml','r') as f:
        grammar = load_grammar(f)

    with open('model/structure.sysml', 'r') as f:
        model = Model().load(f)

    model_pysysml2 = PySysML2Model().from_sysml2_file("model/structure.sysml")

    warehouse = model._get_child("ROOT.Structure.warehouse")

    tree = RenderTree(model_pysysml2)

    print(RenderTree(model_pysysml2, style=AsciiStyle()))

    for pre, fill, node in tree:
        if type(node) is not PySysML2Model:
            print("{}".format(node.name))

    for node in PreOrderIter(model_pysysml2):
        if type(node) is not PySysML2Model:
            print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

    for node in PostOrderIter(model_pysysml2):
        if type(node) is not 'pysysml2.modeling.model.Model':
            print('PostOrderIter: ' + node.name + '( type: ' + str(node.sysml2_type) + ', idx: ' + str(node.idx) + ')')

    for el in model.get("elements", []):
        print(f"Type: {el.get('type')}, Name: {el.get('name')}, ID: {el.get('Add pysysml2id')}")

    model_list = list(NestedDictValues(model))

    items = model.items()

    warehouse = model._get_child("ROOT.Structure.warehouse")

    types = set(el.get("type") for el in model.get("elements", []) if "type" in el)
    print("Element types found in the model:")
    for t in sorted(types):
        print(f"- {t}")

    # Get all Part elements
    parts = [el for el in model.get("elements", []) if el.get("type") == "Part"]
    print(f"Found {len(parts)} parts:")
    for part in parts:
        print(f"- {parts.name} (ID: {parts.id})")

if __name__ == "__main__":
    main()
