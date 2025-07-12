package 'Drone Delivery Service' {
    doc /*  This model descripes a delivery service using drones.
            Drones pick up deliveries from a ware house and transport them to a destination.
        */
    package 'Structure' {
        doc /* This package contains a description of the structure of the system. */
        part 'drone': 'BatteryPoweredDevice';
        part 'warehouse' {
            part 'chargingStation';
            part 'pickupStation';
        }
        part 'control';
    }
    package Types {
        part def 'BatteryPoweredDevice' {
            attribute 'batteryLevel';
        }
        port def 'ElectricPower' {
            doc /* Allows exchange of electrical power */
            attribute aksdj;
        }
        port def 'DeliveryPort' {
            doc /* Allows exchange of deliveries */
        }
    }
}
