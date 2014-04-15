#!/usr/bin/env python

# rFactor Remote LCD
# Copyright (C) 2014 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import SocketServer
import argparse
import time


g_filename = ""


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.fin = open(g_filename, "rb")

        while True:
            request = self.request.recv(1024)

            data = self.fin.read(1024)

            # never run out of data
            if not data:
                self.fin.seek(0)
                data = self.fin.read(1024)

            self.request.sendall(data)
            time.sleep(1.0 / 90.0 / 10.0)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def main():
    try:
        parser = argparse.ArgumentParser(description='rFactor Remote LCD')
        parser.add_argument('HOST', type=str, nargs='?', default="",
                            help='IP to bind to')
        parser.add_argument('PORT', type=int, nargs='?', default=4580,
                            help='PORT to listen on')
        parser.add_argument("-f", "--file", type=str, default="logs/race.log",
                            help="FILE to load and send out")
        args = parser.parse_args()

        global g_filename
        g_filename = args.file

        print "dummy server is listening on %s:%d and sending %s" % (args.HOST, args.PORT, args.file)
        server = ThreadedTCPServer((args.HOST, args.PORT), MyTCPHandler)

        server.serve_forever()
    except:
        raise


if __name__ == '__main__':
    main()


# EOF #
