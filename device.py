import dbus
from dbus import SystemBus
from dbus_properties import Properties

from consts import IFACE,BUS_NAME

class Device(Properties):
    def __init__(self,bus:SystemBus,obj_path,remote_iface) -> None:
        self.bus = bus
        self.device_path = obj_path
        super().__init__(bus,obj_path,remote_iface)

