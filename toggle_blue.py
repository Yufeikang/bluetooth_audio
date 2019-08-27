from blue import find_device, disconnect, connect
import sys
from workflow import Workflow


def main(wf):
    dev_addr, isconnect = sys.argv[1].split('&')
    dev = find_device(address=dev_addr)
    if dev:
        if int(isconnect):
            disconnect(dev)
            print("%s disconnected" % dev.name())
        else:
            connect(dev)
            print("%s connected" % dev.name())
    else:
        print("device not found")

if __name__ == '__main__':
    wf = Workflow()
    wf.run(main)
   
