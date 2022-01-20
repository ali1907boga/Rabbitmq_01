import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='logs',exchange_type='fanout')
result = ch.queue_declare(queue='',exclusive=True)

queue_name = result.method.queue

#binding: match queues and exchanges with eachother
ch.queue_bind(exchange='logs',queue=queue_name)
print('waiting for logs')
def callback(ch,method,properties,body):
    print(f'recieved {body}')
    print(f'{queue_name}')


ch.basic_consume(queue=queue_name,on_message_callback=callback,auto_ack=True)
ch.start_consuming()



