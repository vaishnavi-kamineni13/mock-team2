from django.shortcuts import render,redirect
from .models import Register,Donate,Requests,Count
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        mobilenumber=request.POST['mobilenumber']
        aadhar=request.POST['aadhar']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        
        if password1==password2:  
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already existing')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password1,email=email)
                user.save()
                Register.objects.create(firstname=firstname,lastname=lastname,username=username,email=email,mobilenumber=mobilenumber,aadhar=aadhar,password=password1)
                print('user created')
                return redirect('/')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #sign1=Signup.objects.all()
            return render(request,'index.html')
        else:
            messages.info(request,'Username / password is incorrect')
            return redirect('login')
    else:
        return render(request,'login.html')
def requests(request):
    if request.method=="POST":
        username=request.POST['username']
        item=request.POST['item']
        quantity=request.POST['quantity']
        address=request.POST['address']
        Requests.objects.create(username=username,item=item,quantity=quantity,address=address)
        return redirect('donate')
    else:
        donate1=Donate.objects.all()
        return render(request,'requests.html',{'donate1':donate1})


def donate(request):
    if request.method=='POST':
        username=request.POST['username']
        mobile=request.POST['mobile']
        product=request.POST['product']
        img=request.FILES['img']
        quantity=request.POST['quantity']
        quality=request.POST['quality']
        desc=request.POST['desc']
        
        Donate.objects.create(username=username,mobilenumber=mobile,product=product,img=img,quantity=quantity,quality=quality,desc=desc)
        return redirect('requests')
    else:
        requests1=Requests.objects.all()
        return render(request,'donate.html',{'requests1':requests1})

def about(request):
    return render(request,'about.html')
def logout(request):
    auth.logout(request)
    return redirect('/')