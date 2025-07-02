import socketserver
import socket
from .handler import PLCRequestHandler
from event_logger import logger
import sys

class PLCServer:
    """
    Starts a TCP server on the given port.
    """

    def __init__(self, host: str, port: int):
        logger.info(f"Server starting on {host}:{port}...")
        try:
            self.server = socketserver.ThreadingTCPServer((host, port), PLCRequestHandler)
        except OSError as e:
            logger.exception(f"Failed to bind TCP server on {host}:{port} - {e}")
            sys.exit(1)
        except Exception as e:
            logger.exception(f"Unexpected error while starting TCP server on {host}:{port} – {e}")
            sys.exit(1)

    def start(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        port = self.server.server_address[1]
        logger.info(f"TCP-server now listening on {IPAddr}:{port}")

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Shutdown command received from user - shutting down server...")
            self.server.shutdown()
        finally:
            self.server.server_close()
            logger.info("Server shut down")
