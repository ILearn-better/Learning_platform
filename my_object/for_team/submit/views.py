from django.shortcuts import render,HttpResponse
from pathlib import Path
import os
from for_team import settings
from template.encryption_algorithm.DES import DES



# Build paths inside the project like this: BASE_DIR / 'subdir'.
def submitT(request):
    return render(request,"团队网页.html")
# Create your views here.
def path_return(request):
    # BASE_DIR = Path(__file__).resolve().parent.parent
    print(settings.BASE_DIR)#C:\Users\Administrator\PycharmProjects\my_object\for_team
    print(settings.STATICFILES_DIRS)
    a = [settings.BASE_DIR,'------------------',settings.STATICFILES_DIRS]
    return HttpResponse(a)
#
def teacher_li(request):
    return render(request,"teacher/li_.html")
#
def teacher_zhi(request):
    return render(request,"teacher/li_zhi.html")

def teacher_dai(request):
    return render(request,"teacher/dai.html")


def DESjiami(request):
    if request.method =="GET":
        return render(request,"encryption_algorithm/DES.html")
    if request.method =="POST":
        miyao = request.POST["miyao"]
        p = DES(miyao)
        print(list(request.POST.keys())[-2:])
        try:
            jiami =request.POST["jiami"]
            result_jiami = p.encrypt(jiami)
            return render(request, "encryption_algorithm/DES.html", {"result_jiami":result_jiami})
        except:
            jiemi= request.POST["jiemi"]
            result_jiemi = p.decrypt(jiemi)
            return render(request, "encryption_algorithm/DES.html", {"result_jiemi":result_jiemi})
        print(type(miyao))
        print(request.method)

def deepLeaning(request):
    return render(request,'deepLearn/深度学习.html')
