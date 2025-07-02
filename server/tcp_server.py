import socketserver
from .handler import PLCRequestHandler

class PLCServer:
    """
    Starts a TCP server on the given port.
    """

    def __init__(self, host: str, port: int):
        self.server = socketserver.ThreadingTCPServer((host, port), PLCRequestHandler)

    def start(self):
        print(f"TCP-server started on {self.server.server_address[1]}")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("Server closed.")
        finally:
            self.server.server_close()
