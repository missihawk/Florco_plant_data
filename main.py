from server import PLCServer
from config import Config

if __name__ == "__main__":
    server = PLCServer("0.0.0.0", Config.TCP_PORT)
    server.start()

# Test code
