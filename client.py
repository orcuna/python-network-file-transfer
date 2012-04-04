#!/usr/bin/python
# -*- coding: utf-8 -*-

# Echo client program
import socket

HOST = ''    # The remote host
PORT = 50008          # The same port as used by the server

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()

  parser.add_option("-f", "--filename",
                  metavar="FILE", help="write output to FILE")

  parser.add_option("-i", "--ip",
                  metavar="FILE", help="write output to FILE")

  parser.add_option("-p", "--port",
                  metavar="FILE", help="write output to FILE")


  (options, args) = parser.parse_args()
  filename = options.filename
  ip = options.ip
  port = options.port

  _filename = filename.split('/')[-1]+'.copy'
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, int(port)))
  f = open(filename, 'rb')
  data = f.read()
  f.close()

  data = 'FILENAME=%s=END=%s' % (_filename, data)

  s.send(data)
  s.close()
