#!/usr/bin/python3

from datetime import datetime
from time import sleep
import socket as s
aplist, counter = [], 0


class AccessPoint:
    def __init__(self, type, name, address, port, timeout, attempts):
        self.type = type
        self.name = name
        self.address = address
        self.port = port
        self.timeout = timeout
        self.attempts = attempts
        self.last_change = datetime.now()
        self.state = False
    
    def _helper_(self, state):
        self.last_change = datetime.now()
        self.state = state
    
    def connect(self):
        global counter
        if self.port:
            sock = s.socket(s.AF_INET, s.SOCK_STREAM, s.IPPROTO_TCP)
        else:
            sock = s.socket(s.AF_INET, s.SOCK_RAW, s.IPPROTO_ICMP)
            sock.setsockopt(s.SOL_IP, s.IP_TTL, 64) 
        sock.settimeout(self.timeout)
        try:
            sock.connect((self.address, self.port))
            if not self.state: self._helper_(True)
        except s.error:
            if counter > self.attempts and self.state: self._helper_(False)
            elif counter <= self.attempts and not self.state: self._helper_(True)
        finally: sock.close()


for line in open('/usr/local/etc/apmonit.txt').readlines():
    arr = line.split('; ')
    aplist.append(AccessPoint(type=arr[0], name=arr[1], address=arr[2], port=int(arr[3]), timeout=float(arr[4]), attempts=int(arr[5])))

while True:
    file = open('/var/www/FlaskApp/FlaskApp/result.txt', 'w')
    for item in aplist:
        item.connect()
        file.write('{0}; {1}; {2}; {3}; \r\n'.format(item.type, item.name, item.state, item.last_change.strftime("%Y-%m-%d %H:%M:%S")))
    file.close()
    sleep(60)
 
