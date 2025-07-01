from sysml2py import Model
from sysml2py import load_grammar as loads
from sysml2py.formatting import classtree

def main():
    text = """package Structure {
        // PartDefinition not implemted ;-(
        part def Drone ;

        part drone {
            attribute batteryLevel;

            // portUsage not supported?
            //port power;
        }
        part warehouse {
            part deliveryPackages;
        }
    }"""
    model = loads(text)
    print(classtree(model).dump())

if __name__ == "__main__":
    main()
