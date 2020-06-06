from resources.mqttconnection import createMqttConnection, BusMessage, MqttConnection
from resources.pins import createPins

class BotController():
    def __init__(self, mqtt, pins):
        assert isinstance(mqtt, MqttConnection)
        self.mqtt = mqtt
        self.pins = pins
        self.mqtt.subscribe("Command")
        self.mqtt.setMessageHandler(self.handleMqtt)
    
    def start(self):
        self.mqtt.listen()
    
    def handleMqtt(self, busMessage):
        assert isinstance(busMessage, BusMessage)
        message = busMessage.Message
        if message == "L":
            print("L")
            self.pins.set_pin(0, 1)
        elif message == "LS":
            print("LS")
            self.pins.set_pin(0, 0)
        elif message == "R":
            print("R")
            self.pins.set_pin(0, 1)
        elif message == "RS":
            print("RS")
            self.pins.set_pin(0, 0)
        

def createBotController():
    return BotController(createMqttConnection(), createPins())