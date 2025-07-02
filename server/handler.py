import socketserver
from datetime import datetime

class PLCRequestHandler(socketserver.BaseRequestHandler):
    """
    Handles incoming TCP messages from PLCs.
    """

    def handle(self):
        client_ip = self.client_address[0]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Receive data
        data = self.request.recv(1024)
        print(f"\n[{now}] From {client_ip}:")
        print(f" - Raw Bytes: {data}")

        try:
            decoded = data.decode('utf-8').strip()
            print(f" - Decoded  : {decoded}")
        except UnicodeDecodeError:
            print(" - Could not decode message as UTF-8")
