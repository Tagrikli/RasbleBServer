BUS_NAME = 'org.bluez'
BUS_NAME_OOS = 'com.oos'
ADAPTER_ALIAS = 'Parkolay RPi'


API_PORT = 5000
API_HOST = '127.0.0.1'
class API:
    V1_ROOT = '/api/v1/'
    PASSKEY = V1_ROOT + 'passkey'


class PROP:
    class ADAPTER:
        ADDRESS = 'Address'
        NAME = 'Name'
        ALIAS = 'Alias'
        CLASS = 'Class'
        POWERED = 'Powered'
        DISCOVERABLE = 'Discoverable'
        PAIRABLE = 'Pairable'
        PAIRABLE_TIMEOUT = 'PairableTimeout'
        DISCOVERABLE_TIMEOUT = 'DiscoverableTimeout'
        DISCOVERING = 'Discovering'
        UUIDS = 'UUIDs'
        MODALIAS = 'Modalias'


class CAPABILITY:
    DISPLAY_ONLY = "DisplayOnly"
    DISPLAY_YES_NO = "DisplayYesNo"
    KEYBOARD_ONLY = "KeyboardOnly"
    NO_INPUT_NO_OUTPUT = "NoInputNoOutput"
    KEYBOARD_DISPLAY = "KeyboardDisplay"

class OBJ_PATH:
    ROOT = '/'
    ORG_BLUEZ = '/org/bluez'
    ORG_BLUEZ_HCI0 = '/org/bluez/hci0'
    OOS_AGENT = '/com/oss/agent1'

class IFACE:
    AGENT_MANAGER = 'org.bluez.AgentManager1'
    PROFILE_MANAGER = 'org.bluez.ProfileManager1'
    AGENT = 'org.bluez.Agent1'
    PROFILE = 'org.bluez.Profile1'
    DEVICE = 'org.bluez.Device1'
    DBUS_PROPS = 'org.freedesktop.DBus.Properties'
    ADAPTER = 'org.bluez.Adapter1'
    OBJECT_MANAGER = 'org.freedesktop.DBus.ObjectManager'

#SERVICE_UUID = '00001101-0000-1000-8000-00805F9B34FB'
SERVICE_UUID = 'd5c192d7-764a-47ee-9329-ef1558935f6e'


class LOGGER:
    AGENT = 'AgentLog'
    BTSERVER = 'BTServerLog'

class ERROR_MSG:
    NO_ADAPTER = 'HCI Adapter not found.'
    AGENT_REG = 'Agent could not be registered.'
    AGENT_UNREG = 'Agent could not be unregistered.'

class SUCC_MSG:
    ADAPTER_FOUND = 'HCI Adapter found.'
    ADAPTER_VALID = 'HCI Adapter valid.'
    ADAPTER_CONF_DONE = 'Adapter configuration done.'
    AGENT_REG = 'Agent registered.'
    AGENT_UNREG = 'Agent unregistered'

class INFO_MSG:
    NEW_PAIR = 'New pairing request.'