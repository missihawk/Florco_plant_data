import socketserver
from .handler import PLCRequestHandler

class PLCServer:
    """
    Starts a TCP server on the given port.
    """

    def __init__(self, host: str, port: int):
        self.server = socketserver.ThreadingTCPServer((host, port), PLCRequestHandler)

    def start(self):
        port = self.server.server_address[1]
        print(f"TCP-server started on port {port}")

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("Shutdown command received from user - shutting down server...")
            self.server.shutdown()
        finally:
            self.server.server_close()
            print("Server shut down")
