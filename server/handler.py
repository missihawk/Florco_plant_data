import socketserver
from datetime import datetime
from event_logger import logger

class PLCRequestHandler(socketserver.BaseRequestHandler):
    """
    Handles incoming TCP messages from PLCs.
    """

    def handle(self):
        client_ip = self.client_address[0]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Receive data
        try:
            data = self.request.recv(1024)
            logger.info(f"From {client_ip} - Raw: {data}")

            try:
                decoded = data.decode('utf-8').strip()
                logger.info(f"From {client_ip} - Decoded: {decoded}")
            except UnicodeDecodeError:
                logger.warning(" - Could not decode message as UTF-8")

        except ConnectionResetError:
            logger.warning(f"[{now}] Connection lost from {client_ip}")
        except Exception as e:
            logger.exception(f"[{now}] Unexpected error from {client_ip}: {e}")