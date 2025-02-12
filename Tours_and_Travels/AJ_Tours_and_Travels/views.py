from django.shortcuts import render,redirect
import requests

def index(request):
    return render(request,"index.html")

def about(request):
     return render(request,"about.html")

def service(request):
     return render(request,"service.html")

def contact2(request):
     res = requests.get('http://127.0.0.1:8000/Send_Your_Message').json()
     print("data",res)
     return render(request,"contact.html",{'res':res})

def contact(request):
     import json
     url = "http://127.0.0.1:8000/Send_Your_Message"
     data = {
          'Name': 'Tours & Travels',
          'Email': 'Making a POST request',
          'Phone':  '9130661198',
          'Project' : 'Making a POST request',
          'Subject' :   'This is the data we created.'
          }
     response = requests.post(url, json=data)

     #print(response.json())
     return render(request,"contact.html")
    
#     url = 'http://127.0.0.1:8000/Send_Your_Message'
#     print("url",url)
#     Name = request.POST['Name']
#     Email = request.POST['Email']
#     Phone = request.POST['Phone']
#     payload = {'Name': Name, 'Email': Email, 'Phone': Phone}
#     r = requests.post(url, data=payload)
#     print(r)
#     if r.status_code == 200:
#         print("Failed to register user ", r.status_code)
        





def cars(request):
     return render(request,"cars.html")

def feature(request):
     return render(request,"feature.html")


