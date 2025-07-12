from pysysml2.modeling.model import Model, Port
from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, PostOrderIter

from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

from pathlib import Path

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

    port_defs = {}
    for node in PreOrderIter(model):
        if isinstance(node, Port):
            port_defs[node.name] = node
        # FIXME: grab doc from element_text

    template = env.get_template("README.md.j2")

    with open('README.md', 'w') as file:
        file.write(template.render(port_defs=port_defs))

if __name__ == "__main__":
    main()
