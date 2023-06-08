import random
import requests
import datetime
from time import sleep
from datetime import timedelta
from kafka import KafkaProducer
    
def responseCall_de():
    urlWikide = "https://de.wikipedia.org/w/api.php"
    xend = datetime.datetime.now()
    xend = xend - timedelta(hours=2)
    xstart = xend - timedelta(minutes=1)
    
    paramsde = {
    "action": "query",
    "format": "json",
    "list": "recentchanges",
    "rclimit": 400,
    "rcend": xstart.strftime("%Y-%m-%dT%H:%M:%SZ")  
    }
    
    response_de = requests.get(urlWikide, params = paramsde)
    if response_de.status_code == requests.codes.ok:
        databuff = response_de.json()
        return databuff
    else: print(f"Issue DE: {response_de.status_code}")    
    
    
    
def responseCall_en():
    urlWikien = "https://en.wikipedia.org/w/api.php"
    xend = datetime.datetime.now()
    xend = xend - timedelta(hours=2)
    xstart = xend - timedelta(minutes=1)
    
    paramsde = {
    "action": "query",
    "format": "json",
    "list": "recentchanges",
    "rclimit": 400,
    "rcend": xstart.strftime("%Y-%m-%dT%H:%M:%SZ")  
    }
    
    response_en = requests.get(urlWikien, params = paramsde)
    if response_en.status_code == requests.codes.ok:
        databuff = response_en.json()
        return databuff
    else: print(f"Issue EN: {response_en.status_code}")
    
    
    
    
def main():

        
    bootstrap_servers = 'localhost:9092'
    topic_en = "WikiEdits_EN"
    topic_de = "WikiEdits_DE"
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    
    
    for i in range (20):   
        databuff_en = responseCall_en()
        databuff_de = responseCall_de()  
        changesen = databuff_en["query"]["recentchanges"]
        num_en = str(len(changesen))
        changesde = databuff_de["query"]["recentchanges"]
        num_de = str(len(changesde))
        
        #here is a quick and simple approach:
        # 2 topics for every needed argument or data/input stream
        # has the advantage of a seperated data access
        
        sleep(random.randrange(0,1))
        producer.send(topic_en, value=num_en.encode('utf-8'))
        roducer.send(topic_de, value=num_de.encode('utf-8'))
        #producer.send(topic_en,value=databuff_en)
     
    producer.flush()
    producer.close()
        
    
if __name__ == "__main__":
    main()
    
