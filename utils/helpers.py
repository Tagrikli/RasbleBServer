import dbus
from .consts import IFACE,OBJ_PATH,BUS_NAME,API_PORT,API_HOST


def getEndpoint(path):
    return  f'https://{API_HOST}:{API_PORT}/{path}'

def extractDeviceMAC(device):
    return ":".join(device.split('_')[1:])

def findAdapterPath(bus):
    obj_root = bus.get_object(BUS_NAME,OBJ_PATH.ROOT)
    object_manager = dbus.Interface(obj_root,IFACE.OBJECT_MANAGER)
    managed_objects = object_manager.GetManagedObjects()
    for obj in managed_objects.keys():
        obj_ = obj.split('/')
        if 'hci' in obj_[-1]:
            return obj

if __name__ == '__main__':

    import dbus 
    bus = dbus.SystemBus()
    path = findAdapterPath(bus)
    print(path)