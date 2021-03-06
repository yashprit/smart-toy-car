import logging
import os

DEBUG = os.getenv("ENVIRONEMENT", "DEV") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST", "localhost")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "localhost:9092")
TOPIC = os.getenv("TOPIC", "video-stream-topic")
CLIENT = os.getenv("CLIENT_AGENT", "http://localhost:3001")
logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)