# pip3 install pywhatkit 

import pywhatkit as kit

num = '+54911111111' #your number

msg = 'Hello world' #your messege


try:
    kit.sendwhatmsg(num, msg, 18, 20) # number phone. message , hour , minute
    print('message send')
except:
    print('error')