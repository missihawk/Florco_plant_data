import socketserver
from .handler import PLCRequestHandler
from event_logger import logger

class PLCServer:
    """
    Starts a TCP server on the given port.
    """

    def __init__(self, host: str, port: int):
        self.server = socketserver.ThreadingTCPServer((host, port), PLCRequestHandler)

    def start(self):
        port = self.server.server_address[1]
        logger.info(f"TCP-server started on port {port}")

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Shutdown command received from user - shutting down server...")
            self.server.shutdown()
        finally:
            self.server.server_close()
            logger.info("Server shut down")
