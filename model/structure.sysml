package ROOT {
    package Types {
        part def BatteryPoweredDevice {
            attribute batteryLevel;
        }
    }
    package Structure {
        import Types::*;
        part drone : BatteryPoweredDevice {
        }
        part warehouse {
            part deliveryPackages;
        }
    }
}
