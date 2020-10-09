
from kafka import KafkaConsumer

consumer = KafkaConsumer('corona_news')
for message in consumer:
    print(message)

