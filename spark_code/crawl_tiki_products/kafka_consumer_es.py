from kafka import KafkaConsumer
from elastic_search import *
import json
consumer = KafkaConsumer('sample', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
_es = connect_elasticsearch()
create_index(_es,"tiki_2")

if __name__ == '__main__':
    for message in consumer:
        store_record(_es,"tiki_2",message.value)
