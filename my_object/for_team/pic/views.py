import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .model.model import flower_model
from .models import picture
import cv2

def pr1(request):
    a = settings.BASE_DIR
    # print(a)
    return HttpResponse(a)


def up(request):
    return HttpResponse("OK")

def deepLearning(request):
    return render(request,"index.html")

def upload_file(request):
    if request.method == "GET":
        return render(request, "index.html")
    if request.method == "POST":    # 请求方法为POST时，进行处理
        # name = request.POST["name"]
        myFile =request.FILES.get("photo", None)    # 获取上传的文件，如果没有文件，则默认为None
        print(request.method)
        """
        转码探究
        # code0 = str(myFile.read(),encoding="utf-8")
        # code1=myFile.read()
        # code2 = myFile.read().decode("utf-8")
        # print("code0",type(code0),"code2:",type(code2))
        # with open('./pic/media/'+'code.txt','wb+') as f:
        #     f.write(code1)
        """
        if not myFile:
            return HttpResponse("no files for upload!")
        print(myFile.name)
        print(settings.BASE_DIR)
        lujing_for_show = "/media/"+myFile.name
        # lujing_for_show = os.path.join(os.getcwd(),"pic","media",myFile.name)
        lujing_for_save =os.path.join(os.getcwd(),"pic","media",myFile.name)
        """
        静态模板渲染图片时的路径很重要，路径一定要是settings包含的，不然无法渲染
        """
        try:
            user = picture()
            # user.name = name
            user.photo = lujing_for_save
            user.save()
        except:
            print("erro")
        with open(lujing_for_save, "wb+") as f:
        # with open('./pic/media/'+name+myFile.name, "wb+") as f:
        #     with open(lujing_for_show, "wb+") as f:
                """            
                open的路径要跟着工作路径，index.html的路径要跟着文件路径
                """
                f.write(myFile.read())
        # lujing_for_show =lujing_for_show.replace('\\','/')
        # print(lujing_for_show)
        pre = flower_m(lujing_for_save)
        return render(request,"index.html",{'user':lujing_for_show,'pre':pre})
        # destination = open(os.path.join(os.getcwd(),"media",myFile.name),'wb+') # 打开特定的文件进行二进制的写操作
        # print("over")
        # for chunk in myFile.chunks():      # 分块写入文件
        #     destination.write(chunk)
        # destination.close()
        # return redirect()
#拓展：1.要求每次传完后还可以传，即路由重定向；2.显示传送进度图


def flower_m(dirs):
    f = flower_model()
    dict_=f.predict_fun(dirs)
    return dict_
