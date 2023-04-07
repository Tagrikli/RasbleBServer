import dbus
from dbus.mainloop.glib import DBusGMainLoop
from dbus.exceptions import DBusException

from gi.repository import GLib

from bluez_api.agent import Agent
from bluez_api.adapter import Adapter

from utils.consts import *
from utils.callbacks import *
from utils.helpers import findAdapterPath


DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

# Find bluetooth adapter
ADAPTER_PATH = findAdapterPath(bus)
if not ADAPTER_PATH:
    logger.error(ERROR_MSG.NO_ADAPTER)
    exit(1)
else:
    logger.info(SUCC_MSG.ADAPTER_FOUND, ADAPTER_PATH)

### Adapter Configuration
adapter = Adapter(bus,ADAPTER_PATH,IFACE.ADAPTER)

try:
    # Adapter Object Path mig
    adapter.Get(PROP.ADAPTER.NAME)
    logger.info(SUCC_MSG.ADAPTER_VALID)
except DBusException as e:
    logger.error(e)
    exit(1)

adapter.Set(PROP.ADAPTER.POWERED,True)
adapter.Set(PROP.ADAPTER.DISCOVERABLE,True)
adapter.Set(PROP.ADAPTER.PAIRABLE, True)
adapter.Set(PROP.ADAPTER.DISCOVERABLE_TIMEOUT, dbus.UInt32(0))
adapter.Set(PROP.ADAPTER.PAIRABLE_TIMEOUT, dbus.UInt32(0))
adapter.Set(PROP.ADAPTER.ALIAS, ADAPTER_ALIAS)

logger.info(SUCC_MSG.ADAPTER_CONF_DONE)
###


### Agent Registration
obj_org_bluez = bus.get_object(BUS_NAME,OBJ_PATH.ORG_BLUEZ)
agent_manager = dbus.Interface(obj_org_bluez,IFACE.AGENT_MANAGER)

agent = Agent(bus,OBJ_PATH.OOS_AGENT,BUS_NAME_OOS,cb_passkey)


try:
    agent_manager.RegisterAgent(agent,
                            CAPABILITY.DISPLAY_YES_NO,
                            reply_handler=cb_agent_registered,
                            error_handler=cb_agent_registered_err)
except DBusException as e:
    logger.error(e)
    exit(1)
###


mainloop = GLib.MainLoop()


try:
    mainloop.run()
except KeyboardInterrupt:
    agent_manager.UnregisterAgent(agent,
                                  reply_handler=cb_agent_unregistered,
                                  error_handler=cb_agent_unregistered_err)
    
