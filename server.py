#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import re

HOST = ''
PORT = 50008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print "Connected by:",addr

while 1:
  data = conn.recv(1024)
  if data:
    filename = re.findall('FILENAME=(.*)=END=', data)[0]
    f = open(filename, 'w+')
    data = re.sub('(FILENAME=.*=END=)', '', data)
  if data:
    f.write(data)
    data = ''
  if not data:
    f.close()
    conn.close()
    break
