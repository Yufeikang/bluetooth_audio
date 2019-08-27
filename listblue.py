#! /usr/bin/env python3
import sys
from workflow import Workflow
from blue import get_all_audio_devices, ICON_CONNECTED, ICON_DISCONNECT


def main(wf):
    filter_name = sys.argv[1]
    logger = wf.logger
    for dev in get_all_audio_devices():
        title = dev.name()
        if filter_name:
            if filter_name.upper() not in title.upper():
                continue
        address = dev.getAddressString()
        isconnected = dev.isConnected()
        icon = ICON_CONNECTED if isconnected else ICON_DISCONNECT
        arg = [address, str(isconnected)]
        logger.debug("%s(%s)" % (title, address))
        wf.add_item(
            title=title, subtitle=address, arg='&'.join(arg), valid=True, icon=icon)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()

    sys.exit(wf.run(main))
    # if wf.update_available:
    #     wf.start_update()
