
import dbus
import dbus.service
from utils.consts import IFACE
from .device import Device



def requestPinCode():
    return input(requestPinCode.__name__ + ': ')

def requestPasskey():
    return int(input(requestPasskey.__name__ + ': '))


class Agent(dbus.service.Object):

    def __init__(self, bus, object_path, bus_name, cb_request_confirmation):
        self.bus = bus
        self.device = None
        self.cb_request_confirmation = cb_request_confirmation
        super().__init__(bus, object_path, bus_name)

    def updateDevice(self,device):
        self.device = Device(self.bus,device,IFACE.DEVICE)
        self.device.Set('Trusted',True)
        print('Setted Trusted.')
        

    @dbus.service.method(IFACE.AGENT)
    def Release(self):
        print("Released")

    @dbus.service.method(IFACE.AGENT,in_signature='o',out_signature='s')
    def RequestPinCode(self,device):
        return requestPinCode()

    @dbus.service.method(IFACE.AGENT,in_signature='os')
    def DisplayPinCode(self,device,pincode):
        pass

    @dbus.service.method(IFACE.AGENT,in_signature='o',out_signature='u')
    def RequestPasskey(self,device):
        return requestPasskey()

    @dbus.service.method(IFACE.AGENT,in_signature='ouq')
    def DisplayPasskey(self,device,passkey,entered):
        pass

    @dbus.service.method(IFACE.AGENT,in_signature='ou')
    def RequestConfirmation(self,device,passkey):
        self.cb_request_confirmation(device,passkey)

    @dbus.service.method(IFACE.AGENT,in_signature='o')
    def RequestAuthorization(self,device):
        pass

    @dbus.service.method(IFACE.AGENT,in_signature='os')
    def AuthorizeService(self,device,uuid):
        pass

    @dbus.service.method(IFACE.AGENT)
    def Cancel(self):
        print("Cancelled")

