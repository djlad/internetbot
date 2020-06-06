'''
Creates an MQTT connection with a common interface
Messaging interface matching message-bus-interface:
https://github.com/ecs-global/message-bus-interface/blob/master/messagebus/IMessageBus.cs
'''
from threading import Thread
import paho.mqtt.client as mqtt

class BusMessage():
    def __init__(self, Topic, Message):
        self.Topic = Topic
        self.Message = Message

class MqttConnection():
    def __init__(self, mqttClient, brokerUrl="127.0.0.1"):
        self.client = mqttClient
        self._topicsToSubscribe = set()
        self.messageHandler = self._defaultMessageHandler
        self.thread = Thread(target=self.client.loop_forever, daemon=True)
        self.brokerUrl = brokerUrl
    
    def subscribe(self, topic):
        self._topicsToSubscribe.add(topic)
        self.client.subscribe(topic, qos=2)
    
    def publish(self, topic, payload):
        self.client.publish(topic, payload, qos=2)
    
    def setMessageHandler(self, messageHandlerFunction):
        self.messageHandler = messageHandlerFunction
        self.client.on_message = self.on_message

    def listen(self):
        '''starts listening thread'''
        print("mqtt starting. url: {}".format(self.brokerUrl))
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        connectResult = self.client.connect(self.brokerUrl)
        #self.client.loop_forever()
        self.thread.start()

    def _defaultMessageHandler(self, busMessage):
        print(busMessage.Topic)
        print(busMessage.Message)
    
    def on_connect(self, client, userdata, flags, rc):
        print("connected")
        for topic in self._topicsToSubscribe:
            print("subscribing to: " + topic)
            client.subscribe(topic, qos=2)

    def on_message(self, client, userdata, msg):
        busMessage = BusMessage(msg.topic, msg.payload.decode())
        self.messageHandler(busMessage)

def createMqttConnection():
    broker = "192.168.1.11"
    client = mqtt.Client()
    mqttConnection = MqttConnection(client, broker)
    return mqttConnection