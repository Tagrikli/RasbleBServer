import bluetooth
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from agent import Agent
from consts import BUS_NAME,OBJ_PATH,CAPABILITY,IFACE
from adapter import Adapter
from device import Device

from dbus.mainloop.glib import DBusGMainLoop
def rh():
    print("Agent Registered")

def eh(error):
    print("Err",error)


DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

obj_org_bluez = bus.get_object(BUS_NAME,OBJ_PATH.ORG_BLUEZ)
agent_manager = dbus.Interface(obj_org_bluez,IFACE.AGENT_MANAGER)

agent = Agent(bus,'/com/oos/rasble','com.oos')

agent_manager.RegisterAgent(agent,CAPABILITY.DISPLAY_YES_NO,reply_handler=rh,error_handler=eh)



mainloop = GLib.MainLoop()

try:
    mainloop.run()
except KeyboardInterrupt:
    print("KI")
    agent_manager.UnregisterAgent(agent,reply_handler=rh,error_handler=eh)