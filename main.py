from server import PLCServer
from config import Config

if __name__ == "__main__":
    server = PLCServer(Config.TCP_HOST, Config.TCP_PORT)
    server.start()
