import redis
import json
from datetime import datetime,timedelta

class Redis_DB(object):
    def __init__(self):
        #Input - User Id
        #Output - Result/False

        #Establish Connection
        redis_host = "localhost"
        redis_port = 6379
        redis_password = ""
        self.engine = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

    
    def main(self,uid):
        #red.insert(1,'Hello BK')
        msg = self.retrieve(uid)
        if msg:
            msg_str = msg.decode("utf-8")
            msg_dict = json.loads(msg_str)
            result = self.verify(msg_dict,1)
            if result:
                return msg_dict['Result']
            else:
                return False
        else:
            return False


    def insert(self,uid, result):
        #Inser new records into Redis
        current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        value = {}
        value['Time'] = current_time
        value['Result'] = result
        self.engine.set(uid, json.dumps(value))    
    
    def retrieve(self,uid):
        msg = self.engine.get(uid)
        if msg:
            return msg
        else:
            return None
        
    def verify(self,value,uid):
        #Verify the Last Processed Time. If more than 2 mins reprocess, else use same result
        db_time = datetime.strptime(value['Time'],"%m/%d/%Y %H:%M:%S")
        difference_time = (datetime.now() - db_time).total_seconds()
        if difference_time > 120:
            self.engine.delete(uid)
            return False
        else:
            return True

   
