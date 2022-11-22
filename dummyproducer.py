import time
from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]

topic = "Test"

producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()
data = "hi hello"

def senddata():
    print("test ")
    message = producer.send(topic,bytes(data,"utf-8"))
    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)
    
while True:
    senddata()