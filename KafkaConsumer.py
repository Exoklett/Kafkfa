from kafka import KafkaConsumer
from kafka import KafkaConsumer
from datetime import datetime, timedelta





def main():
    bootstrap_servers = 'localhost:9092'
    topic_en = "WikiEdits_EN"
    topic_de = "WikiEdits_DE"
    
    Consumer_EN = KafkaConsumer(topic_en, bootstrap_servers=bootstrap_servers)
    Consumer_DE = KafkaConsumer(topic_de, bootstrap_servers=bootstrap_servers)
    
    while True:
    
        
        for message in Consumer_EN:
            input = message.value.decode('utf-8')
            print(f"Received message: {input}")
            edits_amounts_en = input
          
        
        for message in Consumer_DE:
            input = message.value.decode('utf-8')
            print(f"Received message: {input}")
            edits_amounts_de = input
            
        
            # from now on, you could use the retrieved data for further data handling
            # for example this quick and dirty MySQL approach
            # conn = mysql.connector.connect(host ="", user ="", ...)
            # cursor = conn.cursor()
            # cursor.execute("INSERT INTO example VALUES(edits_amounts_en, ...)")
            # conn.commit
            
        if not Consumer_EN.assignment() & Consumer_DE.assignment() :
         break   
if __name__ == "__main__":
    main()
    
