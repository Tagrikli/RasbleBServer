BUS_NAME = 'org.bluez'

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

class IFACE:
    AGENT_MANAGER = 'org.bluez.AgentManager1'
    PROFILE_MANAGER = 'org.bluez.ProfileManager1'
    AGENT = 'org.bluez.Agent1'
    DEVICE = 'org.bluez.Device1'
    DBUS_PROPS = 'org.freedesktop.DBus.Properties'
    ADAPTER = 'org.bluez.Adapter1'

