from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from.models import Register
from.models import Homepage

def signup(request):
    if request.method=="POST":
        r=Register(username=request.POST["username"],emailid=request.POST["emailid"],password=request.POST["password"],dob=request.POST["dob"])
        r.save()
        return render(request,"taskapp/signup.html",{"res":"data insertion successfully"})
    return render(request,"taskapp/signup.html")

def login(request):
    if request.method=="POST":
        a = Register.objects.filter(emailid=request.POST["emailid"], password=request.POST["password"])
        if a.count()>0:
            request.session["sessuid"]=request.POST["emailid"]
            if request.POST.get("chk"):
                response = HttpResponse(status=302)
                response.set_cookie('ckey',request.POST["emailid"])
                response.set_cookie('ckey1',request.POST["password"])
                response['Location']='home'
                return response
            
        else:
            return render(request,"taskapp/login.html",{"res":"invalid userid and password"})
    else:
        cookie1=""
        cookie2=""
    if request.COOKIES.get("ckey"):
        cookie1=request.COOKIES["ckey"]
        cookie2=request.COOKIES["ckey1"]

    return render(request,"taskapp/login.html",{"ucookie":cookie1,"pcookie":cookie2})

def home(request):
    if request.method=="POST":
        s = Homepage(sno=request.POST["sno"],size=request.POST["size"],prize=request.POST["prize"],
        emi=request.POST["emi"])
        s.save()
        return render(request,"taskapp/home.html",{"d":Homepage.objects.all(),"msg":"data insert sucessfully...."})
    return render(request,"taskapp/home.html",{"d":Homepage.objects.all()})

    
 
