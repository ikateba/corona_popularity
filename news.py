import requests
import socket
import sys

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def get_news():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=ce6bff91e33146e08ec8cd8bcc4297d2')
    response = requests.get(url)
    return response.json()["articles"]

def send_news_to_spark(articles, tcp_connection):
    for article in articles:
        try:
            full_text = article['content']
            print("News: " + full_text)
            print("..........................")
            tcp_connection.send(full_text.encode())
        except:
            e = sys.exc_info()[1]
            print("Error: %s" % e)


def send_to_consumer(articles):
    for article in articles:
        full_text = article['content']
        if type(full_text) is str:
            producer.send('corona_news', str.encode(full_text))

TCP_IP = "localhost"
TCP_PORT = 9999
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Waiting for TCP connection....")
conn, addr = s.accept()
print("Connected... Starting getting news.")
i = 1
while i == 1:
    resp = get_news()
    send_news_to_spark(resp, conn)
    send_to_consumer(resp)
