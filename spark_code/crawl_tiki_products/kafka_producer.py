from kafka import KafkaProducer
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def produce(topic,message):
    producer.send(topic,message)
    producer.flush()

if __name__ == '__main__':
    producer.send('sample', b'Hello, World!')
    producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
    producer.flush()