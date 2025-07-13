import ScalarValues::*;

package DroneDeliveryService{
    doc
    /*
     * This model descripes a delivery service using drones.
     * Drones pick up deliveries from a ware house and transport them to a destination.
     */

    package Structure{
        doc /* This package contains a description of the structure of the system. */

        part def BatteryPoweredDevice {
            doc /* Device powered by a battery */
            attribute 'askdj' : String;
        }
        part 'Drone Delivery Service' {
            part 'drone': BatteryPoweredDevice;
            part 'warehouse' {
                part 'chargingStation';
                part 'pickupStation';
            }
            part 'control';
        }
    }
}
