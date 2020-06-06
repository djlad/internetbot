from resources.mqttconnection import createMqttConnection, BusMessage, MqttConnection
from resources.pins import set_pin

class BotController():
    def __init__(self, mqtt):
        assert isinstance(mqtt, MqttConnection)
        self.mqtt = mqtt
        self.mqtt.subscribe("Command")
        self.mqtt.setMessageHandler(self.handleMqtt)
    
    def start(self):
        self.mqtt.listen()
    
    def handleMqtt(self, busMessage):
        assert isinstance(busMessage, BusMessage)
        message = busMessage.Message
        if message == "L":
            print("L")
            set_pin(0, 1)
        elif message == "LS":
            print("LS")
            set_pin(0, 0)
        elif message == "R":
            print("R")
            set_pin(0, 1)
        elif message == "RS":
            print("RS")
            set_pin(0,0)
        

def createBotController():
    return BotController(createMqttConnection())