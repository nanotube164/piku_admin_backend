import pika, json

params = pika.URLParameters('amqps://gnibdxxp:4SkiD512SI28LgMrfIP-AobgSRNBaNGv@jackal.rmq.cloudamqp.com/gnibdxxp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    # channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    print('test')