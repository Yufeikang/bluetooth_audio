from AppKit import IOBluetoothDevice


ICON_CONNECTED = 'icon/icon_connected.png'
ICON_DISCONNECT = 'icon/icon_disconnect.png'


def get_all_devices():
    return IOBluetoothDevice.pairedDevices()


def get_all_audio_devices():
    return filter(lambda d: d.isAudioSink(), get_all_devices())


def find_device(name=None, address=None):
    for dev in get_all_devices():
        if name and dev.name() == name:
            return dev
        if address and dev.getAddressString().upper() == address.upper():
            return dev


def disconnect(dev):
    dev.closeConnection()


def connect(dev):
    dev.openConnection()
