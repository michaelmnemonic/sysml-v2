from sysml2py import Model
from sysml2py import load_grammar as loads
from sysml2py.formatting import classtree

def main():
    with open('model/structure.sysml', 'r') as f:
        model = loads(f)
    print(classtree(model).dump())

if __name__ == "__main__":
    main()
