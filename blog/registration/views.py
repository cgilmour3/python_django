from django.shortcuts import render
from registration import forms,models
# Create your views here.
def index(request):
    return render(request, 'index.html')

def regview(request):

    if request.method == "POST":
        registration_form = forms.UserInfoForm(data=request.POST)
        
        if registration_form.is_valid():
            registration_form.save(commit=True)
    
    else:
        print("something went wrong")
    my_dict = {'register: ' : registration_form}
    return render(request,"registration.html", context=my_dict)

def mylogin(request):
    if request.method == "POST":
        login_form = forms.UserLoginForm(data=request.POST)

        if login_form.is_valid():
            login_form.save(commit=True)
    
    else:
        print("something went wrong")
    login_dict = {'userlogin: ' : login_form}
    return render(request,"login.html", context=login_dict)
