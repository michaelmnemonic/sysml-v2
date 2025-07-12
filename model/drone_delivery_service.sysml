package 'Drone Delivery Service' {
    doc /*  This model descripes a delivery service using drones.
            Drones pick up deliveries from a ware house and transport them to a destination.
        */

    private import ScalarValues::*;

    package 'Structure' {
        doc /* This package contains a description of the structure of the system. */

        private import Types::*;

        part 'Drone Delivery Service' {
            part 'drone': 'BatteryPoweredDevice';
            part 'warehouse' {
                part 'chargingStation';
                part 'pickupStation';
            }
            part 'control';
        }
    }
    package Types {
        part def 'BatteryPoweredDevice'{
            doc /* Device powered by a battery */
            attribute 'askdj' : String;
        }
        port def 'ElectricPower' {
            doc /* Allows exchange of electrical power */
            attribute qlwd : String;
        }
        port def 'DeliveryPort' {
            doc /* Allows exchange of deliveries */
            attribute ams : String;
        }
    }
}
