import logging.handlers
from .LoggingHttpServer import LoggingHttpRequestHandler
import SocketServer
import threading


class WebViewHandler(logging.handlers.BufferingHandler):
    def __init__(self, port=8080, capacity=1000, run=True):
        self.port = port
        super(WebViewHandler, self).__init__(capacity=capacity)
        if run:
            self.run()

    def flush(self):
        self.acquire()
        try:
            while self.shouldFlush(None):
                self.buffer.pop(0)
        finally:
            self.release()

    def run(self):
        httpd = SocketServer.TCPServer(("", self.port), LoggingHttpRequestHandler)
        httpd.buffer = self.buffer
        httpd.format = self.format
        t = threading.Thread(target=httpd.serve_forever)
        t.daemon = True
        t.start()
