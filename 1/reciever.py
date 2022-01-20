import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch2 = connection.channel()
ch2.queue_declare(queue='hello')
def call_back(ch,method,properties,body):
    print(f'recieve{body}')
ch2.basic_consume(queue='hello',on_message_callback=call_back,auto_ack=True)
print('waiting for message to exit press ctrl+c')
ch2.start_consuming()









