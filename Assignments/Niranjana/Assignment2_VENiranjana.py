import random
import time
T=int(input('Enter Temperature Limit(15C to 60C):'))
H=int(input('Enter Humidity Limit(30% to 60%):'))
T_alarm=0
H_alarm=0
while(True):
    Temperature=random.uniform(15,60)
    Humidity=random.uniform(30,50)
    print('Temperature is: {0:.2f} C'.format(Temperature))
    print('Humidity is: {0:.2f} %'.format(Humidity))
    time.sleep(1)
    if(Temperature>T and Humidity<H):
        T_alarm=1
        H_alarm=1
        print('Temperature is above the Limit')
        print('Humidity Level is below the limit')
        print('Both alarms are on')
        time.sleep(2)
    elif(Temperature>T):
        T_alarm=1
        H_alarm=0
        print('Temperature is above Limit')
        print('Humidity is above the Limit')
        print('Temperature alarm is on')
        time.sleep(2)
    elif(Humidity<H):
        T_alarm=0
        H_alarm=1
        print('Temperature is within the Limit')
        print('Humidity Level is below the Limit')
        print('Humidity alarm is on')
        time.sleep(2)
    else:
        print('Temperature is below the Limit')
        print('Humidity is above the Limit')
        print('Both alarms are off')
        print("It's a Good weather And Good Day")
        time.sleep(2)



