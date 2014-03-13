#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PSG
#
# Created:     06/03/2014
# Copyright:   (c) PSG 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import http.server

http.server.CGIHTTPRequestHandler.cgi_directories.append('/cgi')

def run(port=8000, server_class=http.server.HTTPServer,handler_class=http.server.CGIHTTPRequestHandler):
    httpd = server_class(('',port),handler_class)
    httpd.serve_forever()

def main():
    try:
        print("Server is starting...")
        run()
    except KeyboardInterrupt:
        print("Server Stopped.")

if __name__ == '__main__':
    main()
