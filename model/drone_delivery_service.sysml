package ROOT {
    package Structure {
        part drone: BatteryPoweredDevice;
        part warehouse {
            part deliveryPackages;
        }
    }
    package Types {
        part def BatteryPoweredDevice {
            attribute batteryLevel;
        }
    }
}
