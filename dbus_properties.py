import dbus
from dbus import SystemBus
from consts import BUS_NAME,IFACE

class Properties:
    def __init__(self,bus:SystemBus,obj_path,remote_iface) -> None:
        self.bus = bus
        self.remote_iface = remote_iface
        self.obj_path = obj_path
        obj = self.bus.get_object(BUS_NAME,obj_path)
        self.iface = dbus.Interface(obj,IFACE.DBUS_PROPS)

    def Get(self,prop):
        return self.iface.Get(self.remote_iface,prop)
    
    def Set(self,prop,value):
        self.iface.Set(self.remote_iface,prop,value)