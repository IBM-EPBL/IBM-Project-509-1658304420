import random
import time
temp_thres=50 #Temperature threshold value
humidity_thres=22 #humidity threshold value 
     
i=0
while(i<10):     
     print(i+1,end="\n")
     temp=random.uniform(1,100)#returns float number
     humidity=random.uniform(1,50)     
     print("Temperature value : {0:.2f}".format(temp)) 
     if temp>temp_thres:
          print("High Temperature")
     else:
          print("Low Temperature")
     print("Humidity value : {0:.2f}".format(humidity))
     if humidity>humidity_thres:
          print("High Humidity")
     else:
          print("Low Humidity")
     i+=1
     
    
 
