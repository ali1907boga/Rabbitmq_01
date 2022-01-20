

#def max_profit(prices):
    #cur_max,max_so_far = 0, 0
    #for i in range(1,len(prices)):
     #   cur_max = max(0,cur_max+prices[i] - prices[i-1])
      #  max_so_far = max(max_so_far,cur_max)
    #return max_so_far
#print(max_profit([7,1,5,3,6,4]))


import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch1 = connection.channel()
ch1.queue_declare(queue='hello')
ch1.basic_publish(exchange='',routing_key='hello',body='hello world')
print('message sent.')
connection.close()














