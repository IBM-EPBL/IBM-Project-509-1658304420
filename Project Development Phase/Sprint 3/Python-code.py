import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {"identity":{"orgId": "jx4tsh",
                        "typeId": "ESP32",
                        "deviceId": "vatsaaa"},
            "auth":{"token": "12345678"}}
client=wiotp.sdk.device.DeviceClient (config=myConfig, logHandlers=None) 
client.connect()
def myCommandCallback(cmd):
     print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
     m=cmd.data['command']
     if(m=="motoron"):
          print ("Motor is switched ON")
     elif(m=="motoroff"):
          print ("Motor is switched OFF")
     print(" ")
while True:
     moisture = random.randint (0, 100) 
     temp = random.randint (0,100)
     humidity = random.randint (0,100)
     flame= random.randint(0,100)
     nitrogen=random.randint(0,100)
     phosporus=random.randint(0,100)
     potassium=random.randint(0,100)
     myData={'moisture': moisture, 'temp': temp, 'humidity': humidity,
             'flame': flame, 'nitrogen': nitrogen, 'phosporus': phosporus, 'potassium': potassium}
     client.publishEvent (eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
     print("Published data Successfully: %s", myData)
     time.sleep (2)
     client.commandCallback = myCommandCallback
client.disconnect()
