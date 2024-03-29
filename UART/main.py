import sys
from Adafruit_IO import MQTTClient
import time
import random
# from simple_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "datnguyenvan"
AIO_KEY = "aio_HYFy92qhIr7dT3d2n23yWdmwrdjr"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5

ai_result = ""
pre_result = ""

while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     print("Random data is being published...")
    #     temp = random.randint(15, 60)
    #     client.publish("cambien1", temp)
    #     light = random.randint(0, 500)
    #     client.publish("cambien2", light)
    #     humid = random.randint(0, 100)
    #     client.publish("cambien3", humid)

    # counter_ai = counter_ai - 1
    # if counter_ai <= 0:
    #     counter_ai = 5
    #     pre_result = ai_result
    #     ai_result = image_recognizer()
    #     print("AI Output: ", ai_result)
    #     if pre_result != ai_result:
    #         client.publish("ai", ai_result)

    readSerial(client)

    time.sleep(1)