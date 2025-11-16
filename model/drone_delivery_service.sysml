package DroneDeliveryService {
    doc /* High-level system architecture for a drone-based delivery service with automated package transportation, battery management, and logistics coordination */

    package Structure {
        doc /*System architecture defining core components and relationships, including drones, warehouses, and control systems */

        package Elements {
            doc /* Elements of the system */

            private import DroneDeliveryService::Structure::Types::*;

            part 'Drone Delivery Service' {
                doc /* Complete delivery system with drone fleet, warehouse infrastructure, and centralized control for logistics management */
                part 'Drone' : 'Battery powered device'  {
                    doc /* Represents an individual autonomous drone used for package delivery, equipped with navigation systems, battery, and payload capacity */
                    port 'Power port'  {
                        doc /* Electrical interface for charging drone's battery, supporting wired/wireless charging and status monitoring */
                    }
                    port 'Delivery holder' {
                        doc /* Mechanical interface for automated package handling with weight/size verification and navigation integration */
                    }
                }
                part 'Warehouse' {
                    doc /* Central logistics hub managing drone operations and package storage with maintenance stations */
                    part 'Charging station' {
                        doc /* Automated charging infrastructure with wireless pads, health monitoring, queue management, and backup power */
                    }
                    part 'Pickup station' {
                        doc /* Operational hub for drone deployment with automated docking, conveyors, status checks, and route assignments  */
                    }
                }
                part 'Control' {
                    doc /* Centralized management system for real-time tracking, route optimization, package prioritization, fleet allocation, and warehouse integration  */
                }
            }
        }
        package Types {
            doc /* Types used in structure model */

            part def 'Battery powered device' {
                doc /* Device powered by a pattery */
                attribute 'State of Charge' {
                    doc /* State of Charge (SOC) of the device representing a measure of the power avaible to power the device*/
                }
                attribute isCharging {}
            }   
        }
    }
}