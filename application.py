seimport os
from flask import Flask,redirect,render_template,request
import time
import mysql.connector
import random
import urllib
import datetime
import json
import pickle
import hashlib
import requests
application = Flask(__name__,template_folder='templates',static_folder='static')
# server = 'aashish.ccftqt1uftij.us-east-1.rds.amazonaws.com'
# database = 'adb'
# username = 'aashishgk'
# password = 'aashishgk7760'
# driver= '{ODBC Driver 13 for SQL Server}'
port = 3000
# cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)


# @application.route('/')
# def hello_world():
#   return render_template('index.html')
   
# def disdata():
#     mydb = mysql.connector.connect(host="aashishgk.ccftqt1uftij.us-east-1.rds.amazonaws.com",user="aashi",password="aashishgk7760")
#     print(mydb)
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * from adb.quakes")
#   #  cursor = cnxn.cursor()
#   #  start = time.time()
#   #  cursor.execute("SELECT TOP 10000 * FROM quakes")
#     row = mycursor.fetchall()
#   #  end = time.time()
#   #  executiontime = end - start
#     return render_template('searchearth.html',ci=row)
# def randrange_time(rangfro=None, rangto=None, num=None):
#     dbconn = mysql.connector.connect(host="aashishgk.ccftqt1uftij.us-east-1.rds.amazonaws.com",user="aashi",password="aashishgk7760")
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0, int(num)):
#         mag1 = round(random.uniform(rangfro, rangto), 1)
#         mag2 = round(random.uniform(rangfro, rangto), 1)
#         if mag1 > mag2:
#             success = "SELECT * from adb.quakes " # where depth>'" + str(mag2) + "' and depth <'" + str(mag1)
#         else:
#             success = "SELECT * from adb.quakes"# where depth>'" + str(mag1) + "' and depth <'" + str(mag2)
#         # Do MySQL query
#         print("Execution failed")
#         cursor.execute(success)
#         data = cursor.fetchall()
#         print(data)
#         rows = []
#         row_count = 0
#         for j in data:
#             print(j)
#             row_count = j
#             rows.append(str(j))
#             new_row = rows
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
#             first_execute) + "The count is " + str(row_count)
#         final.append(check123)
#         print(first_execute)

#         # print(new_row)
#         # print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     #print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count123.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)
# def randrange(rangefrom=None,rangeto=None,num=None):
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0,int(num)):
#         mag1= round(random.uniform(rangefrom, rangeto),1)
#         mag2 = round(random.uniform(rangefrom, rangeto),1)
#         if mag1 > mag2:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag2) + "' and mag <" + str(mag1)
#         else:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag1) + "' and mag <" + str(mag2)


#         print(mag1)
#         print(mag2)
#         hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
#         key = "redis_cache:" + hash

#         if (r.get(key)):
#            print("redis cached")
#         else:
#             print(key)
#             print(r)
#            # Do MySQL query
#             print("Execution failed")
#             cursor.execute(success)
#             data = cursor.fetchall()
#             rows = []
#             row_count = 0
#             for j in data:
#                 print(j)
#                 row_count = j
#                 rows.append(str(j))
#                 new_row = rows
#             # Put data into cache for 1 hour
#             r.set(key, pickle.dumps(list(rows)) )
#             r.expire(key, 36);

#         #if (i < 1):
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 "+str(mag1)+" The Depth 2 "+str(mag2)+" The time is "+ str(first_execute)+"The count is "+str(row_count)
#         final.append(check123)
#         print(first_execute)

#             #print(new_row)
#             #print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     #print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count.html', t=final,u=mag2_li, s= timeq,ci = rows, en=exectime)


# def randrange_time(rangfro=None,rangto=None,num=None):
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0,int(num)):
#         mag1= round(random.uniform(rangfro, rangto),1)
#         mag2 = round(random.uniform(rangfro, rangto),1)
#         if mag1 > mag2:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag2) + "' and mag <" + str(mag1)
#         else:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag1) + "' and mag <" + str(mag2)
#        # Do MySQL query
#         print("Execution failed")
#         cursor.execute(success)
#         data = cursor.fetchall()
#         rows = []
#         row_count = 0
#         for j in data:
#             print(j)
#             row_count = j
#             rows.append(str(j))
#             new_row = rows
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 "+str(mag1)+" The Depth 2 "+str(mag2)+" The time is "+ str(first_execute)+"The count is "+str(row_count)
#         final.append(check123)
#         print(first_execute)

#             #print(new_row)
#             #print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     #print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count123.html', t=final,u=mag2_li, s= timeq,ci = rows, en=exectime)


# def randrange_out(rangfro=None,rangto=None,num=None):
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0,int(num)):
#         mag1= round(random.uniform(rangfro, rangto),1)
#         mag2 = round(random.uniform(rangfro, rangto),1)
#         if mag1 > mag2:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag2) + "' and mag <" + str(mag1)
#         else:
#             success = "SELECT count(*) from [quakes] where mag>'" + str(mag1) + "' and mag <" + str(mag2)


#         print(mag1)
#         print(mag2)
#         hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
#         key = "redis_cache:" + hash

#         if (r.get(key)):
#            print("redis cached")
#         else:
#             print(key)
#             print(r)
#            # Do MySQL query
#             print("Execution failed")
#             cursor.execute(success)
#             data = cursor.fetchall()
#             rows = []
#             row_count = 0
#             for j in data:
#                 print(j)
#                 row_count = j
#                 rows.append(str(j))
#                 new_row = rows
#             # Put data into cache for 1 hour
#             r.set(key, pickle.dumps(list(rows)) )
#             r.expire(key, 36);

#         #if (i < 1):
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 "+str(mag1)+" The Depth 2 "+str(mag2)+" The time is "+ str(first_execute)+"The count is "+str(row_count)
#         final.append(check123)
#         print(first_execute)

#             #print(new_row)
#             #print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     #print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count1.html', t=final,u=mag2_li, s= timeq,ci = rows, en=exectime)


# def randrange1(rangfro=None,rangto=None,lat1=None):
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()

#     success="SELECT latitude,longitude,time,mag from [quakes] where mag>'"+str(rangfro)+"' and mag <'"+str(rangto)\
#             +"' and latitude>"+str(lat1)

#     print("Execution failed")
#     cursor.execute(success)
#     data = cursor.fetchall()
#     print("Step4")
#     print(data)
#     return render_template('searchearth.html',ci = data)

# def searchdata(magone=None,magtwo=None,split=None):
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     print(split)
#     mag1 = int(magone)
#     mag2 = int(magtwo)
#     diff = (mag2- mag1)/int(split)
#     print(diff)
#     rows=[]
#     while(mag1 < int(magtwo)):
#         print(mag1)
#         mag2 = mag1+diff
#         sql="SELECT count(*) from [quakes] where mag BETWEEN'" + str(mag1) + "' and " + str(mag2)
#         cursor.execute(sql)
#         data=cursor.fetchall()
#         print(data)
#         for j in data:
#             print('in for')
#             rows.append(j)
#             print(rows)
#         mag1 = mag2
#         print(mag2)
    #     hash = hashlib.sha224(sql.encode('utf-8')).hexdigest()
    #     key = "redis_cache:" + hash

    #     if (r.get(key)):
    #        print("redis cached")
    #     else:
    #         print(key)
    #         print(r)
    #        # Do MySQL query
    #         print("Execution failed")
    #         cursor.execute(sql)
    #         data = cursor.fetchall()
    #         rows = []
    #         row_count = 0
    #         for j in data:
    #             print(j)
    #             row_count = j
    #             rows.append(str(j))
    #             new_row = rows
    #         # Put data into cache for 1 hour
    #         r.set(key, pickle.dumps(list(rows)) )
    #         r.expire(key, 36);

    #     #if (i < 1):
    #     first_time = time.time()
    #     first_execute = first_time - start
    #     timeq.append(first_execute)
    #     check123 = "The Depth 1 "+str(mag1)+" The Depth 2 "+str(mag2)+" The time is "+ str(first_execute)+"The count is "+str(row_count)
    #     final.append(check123)
    #     print(first_execute)
    #     cursor.execute(sql)
    # print("Step4")
    # end = time.time()
    # exectime = end - start
    # return render_template('results.html', data=rows)


# def longi(longi=None):
#     mydb = mysql.connector.connect(host="aashishgk.ccftqt1uftij.us-east-1.rds.amazonaws.com",user="aashi",password="aashishgk7760")
#     mycursor = mydb.cursor()
#     mycursor.execute(" ")
#   #  cursor = cnxn.cursor()
#   #  start = time.time()
#   #  cursor.execute("SELECT TOP 10000 * FROM quakes")
#     rows = mycursor.fetchall()
#     return render_template('long.html',bi = rows)

# def ccode(code=None):
#     dbconn = pyodbc.connect(
#         'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     success = "SELECT * from [quakes] "
#     #"SELECT * from sp where code = '" + rangfro + "'"
#     print("Execution failed")
#     cursor.execute(success)
#     data = cursor.fetchall()
#     print("Step4")
#     print(data)
#     end = time.time()
#     exectime = end - start
#     return render_template('codes.html', ci=data, en=exectime )

# def ques81(elevfrom=None,elevto=None):
#     dbconn = pyodbc.connect(
#         'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     success = "SELECT Number, Country, latitude, longitude, elev from [vc] WHERE Elev > '"+str(elevfrom)+"' and elev<'"+str(elevto)+"'"
#     #"SELECT * from sp where code = '" + rangfro + "'"
#     print("Execution failed")
#     cursor.execute(success)
#     data = cursor.fetchall()
#     print("Step4")
#     print(data)
#     end = time.time()
#     exectime = end - start
#     return render_template('codes.html', ci=data, en=exectime )

# def ques10A(elevfrom=None,elevto=None,num=None):
#     dbconn = pyodbc.connect(
#         'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     for i in range(0, int(num)):
#         success = "SELECT Number, Country, latitude, longitude, elev from [vc] WHERE Elev > '"+str(elevfrom)+"' and elev<'"+str(elevto)+"'"
#         print("Execution failed")
#         cursor.execute(success)
#         data = cursor.fetchall()
#     end = time.time()
#     exectime = end - start
#     return render_template('codes.html', ci=data, en=exectime )


# def ques11A(elevfrom=None,elevto=None,num=None):
#     dbconn = pyodbc.connect(
#         'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = dbconn.cursor()
#     start = time.time()
#     for i in range(0, int(num)):
#         success = "SELECT Number, Country, latitude, longitude, elev from [vc] WHERE Elev > '"+str(elevfrom)+"' and elev<'"+str(elevto)+"'"
#         cursor.execute(success)
#         data = cursor.fetchall()
#     hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
#     key = "redis_cache:" + hash
#         # print(key)
#     if (r.get(key)):
#         print("redis cached")
#     #    print("r"+key)
#     else:
#     # Do MySQL query
#         print("Execution failed")
#         cursor.execute(success)
#         data = cursor.fetchall()
#         rows = []
#         row_count = 0
#         for j in data:
#             # print(j)
#             row_count = j
#             rows.append(str(j))
#             new_row = rows
#         # Put data into cache for 1 hour
#         r.set(key, pickle.dumps(list(rows)) )
#         r.expire(key, 36);
    
#     end = time.time()
#     exectime = end - start

#     return render_template('codes.html', ci=data, en=exectime )


# @application.route('/magval', methods=['GET'])
# def magval():
#     dbconn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#     mag = request.args.get('magone', '')
#     magtwo = request.args.get('magtwo', '')
#     split = request.args.get('split','')
#     return searchdata(mag,magtwo,split)

# @application.route('/displaydata', methods=['GET'])
# def display():
#     return disdata() 

# @application.route('/multiplerun', methods=['GET'])     
# def randquery():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     num = request.args.get('nom')
#     return randrange(rangfro, rangto, num)

# @application.route('/multiplerun567', methods=['GET'])
# def randquery_out():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     num = request.args.get('nom')
#     return randrange_out(rangfro,rangto,num)


# @application.route('/multiplerun123', methods=['GET'])
# def randquery123():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     num = request.args.get('nom')
#     return randrange_time(rangfro,rangto,num)


# @application.route('/multiplerun1', methods=['GET'])
# def randquery1():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     lat1 = float(request.args.get('lat'))
#     return randrange1(rangfro,rangto,lat1)

# @application.route('/routeone', methods=['GET'])
# def routeone():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     num = request.args.get('nom')
#     print("in button")
#     val = request.args.get('submit_button')
#     print(val) 
#     if val=='0':
          
#             print("do something")
#             return randrange_time(rangfro,rangto,num)
#     elif val=='1': 
#             print("Do else")
#             return randrange_out(rangfro,rangto,num)
    
# @application.route('/routetwo', methods=['GET'])
# def routetwo():
#     long = float(request.args.get('long'))
#     return longi(long)
# @application.route('/sample', methods=['GET'])  # countrycode
# def countrycode():
#     longi = float(request.args.get('longi'))

#     return longi(longi)
# @application.route('/ques8', methods=['GET'])          #time
# def ques8():
#     elevfrom = int(request.args.get('elevfrom'))
#     elevto = int(request.args.get('elevto'))
#     return ques81(elevfrom, elevto)

# @application.route('/ques10', methods=['GET'])          #time
# def ques10():
#     elevfrom = int(request.args.get('elevfrom'))
#     elevto = int(request.args.get('elevto'))
#     num = int(request.args.get('num'))

#     return ques10A(elevfrom, elevto,num)


# @application.route('/ques11', methods=['GET'])          #time
# def ques11():
#     elevfrom = int(request.args.get('elevfrom'))
#     elevto = int(request.args.get('elevto'))
#     num = int(request.args.get('num'))

#     return ques11A(elevfrom, elevto,num)
# @application .route('/multiplerun123', methods=['GET'])  # without redis/memcache extract
# def randquery123():
#     rangfro = float(request.args.get('rangefrom'))
#     rangto = float(request.args.get('rangeto'))
#     num = request.args.get('nom')
#     return randrange_time(rangfro, rangto, num)

# @application .route('/image', methods=['GET'])
# def image():
#   start = time.time()
#   print(start)
#   gh=int(start)%2
#   print(gh)
#   return render_template("image.html",ai=gh)
@application.route('/')
def hello_world():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print(ip)
    return render_template("index.html", ip=ip)




if __name__ == '__main__':
  application.run(port=port)
