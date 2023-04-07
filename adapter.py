from dbus_properties import Properties



class Adapter(Properties):
    def __init__(self, bus, obj_path,remote_iface) -> None:
        super().__init__(bus, obj_path,remote_iface)