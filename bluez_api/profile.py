import dbus
import dbus.service
from utils.consts import IFACE
import os


class Profile(dbus.service.Object):

    def __init__(self, bus=None, object_path=None, bus_name=None):
        self.bus = bus
        super().__init__(bus, object_path, bus_name)

    @dbus.service.method(IFACE.PROFILE)
    def Release(self):
        print('Released')


    @dbus.service.method(IFACE.PROFILE,in_signature='oha{sv}')
    def NewConnection(self,device,fd,properties):
        self.fd = fd.take()
        print('NewConnection({}, {})'.format(device, self.fd))

        
        print(self.fd)

        for key in properties.keys():
            if key == 'Version' or key == 'Features':
                    print('  {} = 0x{:04x}'.format(key, properties[key]))
            else:
                    print('  {} = {}'.format(key, properties[key]))


    @dbus.service.method(IFACE.PROFILE,in_signature='o')
    def RequestDisconnection(self, path):
        print('RequestDisconnection {}'.format(path))

        if self.fd > 0:
            os.close(self.fd)
            self.fd = -1
