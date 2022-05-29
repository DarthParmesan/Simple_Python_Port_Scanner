import socket
import sys
from datetime import datetime


class Scanner:

    def __init__(self):
        pass

    def isOpen(self, target, port):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            conn = s.connect_ex((target, port))

            if conn == 0:
                s.close()
                return True
            else:
                return False

        except socket.gaierror:
            print("socket.gaierror")
            sys.exit()
        except socket.error:
            print("socket.error")
            sys.exit()



    def scan(self, target, start, end):

        ports = []

        starttime = datetime.now()
        for port in range(int(start), int(end)+1):
            print("Checking Port >> " + str(port))
            if self.isOpen(target, port):
                print("port {} is open".format(port))
                ports.append(port)


        endtime = datetime.now()
        elapsed = endtime - starttime

        return ports, elapsed