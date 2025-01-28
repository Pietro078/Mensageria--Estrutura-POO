import pika;

class RabbitMQ_publicher():
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__chaneel = self.creat_chanel()
     
        

    def creat_chanel(self):
        conection_paramters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password)
        )
        chanel = pika.BlockingConnection(conection_paramters).channel()
        
        chanel.basic_publish(
            exchange="treinoExchend",
            routing_key="",
            body=input("mensagem: "),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
           
        )
    def start(self):
        self.__chaneel
        print("iniciando")

rabitMQ_piblicher = RabbitMQ_publicher()
rabitMQ_piblicher.start()