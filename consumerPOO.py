import pika

class RabbitMQ_consumer():
    def __init__(self, minha_calbeck) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "minhaFila"
        self.__calbeck = minha_calbeck
        self.__chanel = self.creat_chanel()

    def creat_chanel(self):
        conection_paramters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
    )
        chanel = pika.BlockingConnection(conection_paramters).channel()

        chanel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        chanel.basic_consume(
            queue="minhaFila",
            auto_ack=True,
            on_message_callback=self.__calbeck
        )
        return chanel
    
    def start(self):
        print("iniciando o consumer da queue")
        self.__chanel.start_consuming()

def minha_calbeck(ch,method,propierties,body):
    print(body)


rabittMQ_consumer = RabbitMQ_consumer(minha_calbeck)
rabittMQ_consumer.start()
