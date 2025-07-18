from pysysml2.modeling.model import Model, Port, Doc
from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, PostOrderIter

from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

from pathlib import Path

def get_port_defs(model):
    port_defs = {}
    for node in PreOrderIter(model):
        if isinstance(node, Port):
            description = ""
            for sibling in node.siblings:
                if isinstance(sibling, Doc):
                    description += str(sibling.element_text)
            port_defs[node.name] = {'description': description.strip()}
    return port_defs

def main():
    # load model
    model = Model().from_sysml2_file("model/drone_delivery_service.sysml")

    model.to_png()

    # Set up the Jinja2 environment for template rendering
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(),
        lstrip_blocks = True,
        trim_blocks= True
    )

    template = env.get_template("README.md.j2")

    with open('README.md', 'w') as file:
        file.write(template.render(port_defs=get_port_defs(model)))

if __name__ == "__main__":
    main()
