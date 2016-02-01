#!/usr/bin/python
#adaptado por Moisés Cardona http://moisescardona.net
#trabajo original: http://thenextweb.com/shareables/2016/01/31/frustrated-comcast-customer-sets-up-bot-to-tweet-complaints-every-time-internet-speed-drops/
#codigo del trabajo original: http://pastebin.com/WMEh802V
import os
import sys
import csv
import datetime
import time
import requests
 
def test():
 
        #run speedtest-cli
        print 'running test'
        a = os.popen("python /home/pi/Documents/speedtest-cli --simple").read()
        print 'ran'
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u
        #save the data to file for local network plotting
        out_file = open('/home/pi/Documents/data.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,p,d,u))
        out_file.close()
 
        #connect to facebook
     	face_token = 'YOUR_ID' #Sustituye YOUR_ID por el ID del app que debes crear en https://developers.facebook.com/	
	libertypageid = '155802867766659' #este es el ID de la pagina de liberty, pero puedes cambiarlo al ID de Claro o cualquier otro proveedor. Puedes conseguir el ID de la pagina en http://findmyfbid.com/

        #try to post to Liberty Page if speedtest couldnt even connet. Probably wont work if the internet is down
        if "Cannot" in a:
                try:
			post = 'Hola Liberty, por que no tengo internet? Pago por 40down\\4up en Carolina... Por favor resuelvanme!!'
			post.replace(' ', '+')
			requests.post("https://graph.facebook.com/" + libertypageid + "/feed/?message=" + post + "&access_token=" + face_token)
                except:
                        pass
 
        # post to Liberty Page if down speed is less than whatever I set
        elif eval(d)<30:
                print "trying to Post to Facebook Page"
                try:
                        # i know there must be a better way than to do (str(int(eval())))
			post = 'Hola Liberty, por que mi velocidad de internet es " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up cuando pago por 40down\\4up en Carolina... Por favor resuelvanme!!'
			post.replace(' ', '+')
			requests.post("https://graph.facebook.com/" + libertypageid + "/feed/?message=" + post + "&access_token=" + face_token)
                except Exception,e:
                        print str(e)
                        pass
	elif eval(d)>=30:
		print "trying to Post to Facebook Page"
                try:
                        # i know there must be a better way than to do (str(int(eval())))
			post = 'Hola Liberty, Gracias por ofrecerme un servicio de excelencia. Pago por 40down\\4up en Carolina y estoy recibiendo la velocidad completa.'
			post.replace(' ', '+')
			requests.post("https://graph.facebook.com/" + libertypageid + "/feed/?message=" + post + "&access_token=" + face_token)
                except Exception,e:
                        print str(e)
                        pass
        return
       
if __name__ == '__main__':
        test()
        print 'completed'
