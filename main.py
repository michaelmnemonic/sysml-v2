from sysml2py import Attribute, Part, Item, Model, Package

def main():
    with open("model/structure.sysml", "r") as f:
        model = Model().load(f)

    print(model.dump())

if __name__ == "__main__":
    main()
