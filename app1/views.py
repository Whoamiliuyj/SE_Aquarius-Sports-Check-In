from django.shortcuts import render, HttpResponse, redirect
from .models import user_info
from .models import Sp_table
from .models import Target_set
from .models import community
from .models import activity
from .models import admin_info
from .models import images
#
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
from datetime import datetime, timedelta
import pytz
from django.db.models import Count
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from apscheduler.triggers.interval import IntervalTrigger
#
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache  # 使用Django缓存
import random
import string
import time
import hashlib
#
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.schemas import AutoSchema
from django.utils.decorators import  method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
#
from urllib.request import urlretrieve
from django.core.files import File
from io import BytesIO
from PIL import Image
#
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
from urllib.parse import urljoin
import os
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

from django.http import HttpResponse
import urllib.request
import requests
from urllib.parse import urlencode
from github import Github


ngrok = "https://d566-2001-250-206-e69b-c0ce-351b-7982-df67.ngrok-free.app/api/download/"

## pip install celery
## pip install pytz
## pip install django-cors-headers
## pip install mysqlclient
## pip install apscheduler

# Create your views here.

#test
def django_mysql_test(request):
    current_time = datetime.now()
    current_time_utc = pytz.utc.localize(current_time)
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    T = current_time_utc.astimezone(beijing_timezone)
    #new
    # for i in range(1,6) :
    #     admin_info.objects.create(user_name = i,
    #                               user_mail = '0000'+str(i)+'@buaa.edu.cn',
    #                               user_password = '123456789',
    #                               user_uid = 41182600+i,
    #                               user_academy = id2fac(31182600+i),
    #                               user_num = i,
    #                               )
    # for i in range(6,11) :
    #     admin_info.objects.create(user_name = i,
    #                               user_mail = '0000'+str(i)+'@buaa.edu.cn',
    #                               user_password = '123456789',
    #                               user_uid = 41180000+i*2*10000+i,
    #                               user_academy = id2fac(31180000+i*2*10000+i),
    #                               user_num = i,
    #                               )  
    # admin_info.objects.create(user_name = 0,
    #                               user_mail = '0000@buaa.edu.cn',
    #                               user_password = '12345678',
    #                               user_uid = 0,
    #                               user_academy = 0,
    #                               user_num = 0,
    #                               )    
    # for i in range (1,6) :
    #     user_info.objects.create( user_name = str(i)+str(i),
    #                               user_mail = '1000'+str(i)+'@buaa.edu.cn',
    #                               user_password = '123456789',
    #                               user_uid = 31182600+i,
    #                               user_academy = id2fac(31182600+i),
    #                               user_gender = True,
    #                               user_time_a = 10-i,
    #                               user_num = i,
    #                               user_sp_num = 7-i,
    #                               user_rtime = T,
    #                               )
    
    # for i in range (6,11) :
    #     user_info.objects.create( user_name = str(i)+str(i),
    #                               user_mail = '1000'+str(i)+'@buaa.edu.cn',
    #                               user_password = '123456789',
    #                               user_uid = 31180000+i*2*10000+i,
    #                               user_academy = id2fac(31180000+i*2*10000+i),
    #                               user_gender = True,
    #                               user_time_a = 16-i,
    #                               user_num = i,
    #                               user_sp_num = 14-i,
    #                               user_rtime = T,
    #                               )

    # user_info.objects.create( user_name = 1,
    #                               user_mail = '1@1.cn',
    #                               user_password = '1',
    #                               user_uid = 11111111,
    #                               user_academy = 11,
    #                               user_gender = True,
    #                               user_time_a = 1,
    #                               user_num = 1,
    #                               user_sp_num = 1,
    #                               user_rtime = T,
    #                               )    
        
    for i in range (1,4):
        Sp_table.objects.create( user_name = '111',
                                 user_mail = '10001@buaa.edu.cn',
                                 user_uid = 31182601,
                                 sp_pid = i,
                                 sp_id = i,
                                 sp_type = '跑步',
                                 sp_date = T,
                                 sp_time_begin = T,
                                 sp_time_end = T+timedelta(hours=2),
                                 sp_time = 2,
                                 sp_location = 'buaa_'+str(i),
                                 sp_message = '111222333_'+str(i),
                                 sp_love_n = i,

                                 )

    for i in range (4,7):
        Sp_table.objects.create( user_name = '111',
                                 user_mail = '10001@buaa.edu.cn',
                                 user_uid = 31182601,
                                 sp_pid = i,
                                 sp_id = i,
                                 sp_type = '跑步',
                                 sp_date = T,
                                 sp_time_begin = T,
                                 sp_time_end = T+timedelta(hours=1),
                                 sp_time = i,
                                 sp_location = 'buaa_'+str(i),
                                 sp_message = '111222333_'+str(i),
                                 sp_love_n = i,
                                 
                                 )
    for i in range (7,11):
        Sp_table.objects.create( user_name = '111',
                                 user_mail = '10001@buaa.edu.cn',
                                 user_uid = 31182602,
                                 sp_pid = i,
                                 sp_id = i,
                                 sp_type = '篮球',
                                 sp_date = T,
                                 sp_time_begin = T,
                                 sp_time_end = T+timedelta(hours=2),
                                 sp_time = 2,
                                 sp_location = 'buaa_'+str(i),
                                 sp_message = '111222333_'+str(i),
                                 sp_love_n = i,

                                 )
    for i in range (11,13):
        Sp_table.objects.create( user_name = '111',
                                 user_mail = '10001@buaa.edu.cn',
                                 user_uid = 31182603,
                                 sp_pid = i,
                                 sp_id = i,
                                 sp_type = '足球',
                                 sp_date = T,
                                 sp_time_begin = T,
                                 sp_time_end = T+timedelta(hours=2),
                                 sp_time = 2,
                                 sp_location = 'buaa_'+str(i),
                                 sp_message = '111222333_'+str(i),
                                 sp_love_n = i,

                                 )
            
    return HttpResponse('create success')


def admin_create(resquest):
    admin_info.objects.create(user_name = 'admin0',
                              user_mail = '21182645@buaa.edu.cn',
                              user_password = '12345678',
                              user_uid = 21182645,
                              user_academy = 0,
                              user_num = 0,
                              )
    for i in range(1,47) :
        admin_info.objects.create(user_name = 'admin'+ str(i),
                                  user_mail = '0000'+str(i)+'@buaa.edu.cn',
                                  user_password = '123456789',
                                  user_uid = 21000000+i*10000,
                                  user_academy = id2fac(21000000+i*10000),
                                  user_num = i,
                                  )
    return HttpResponse('create success')    


def delete_sql_data(request):

    current_time = datetime.now()
    current_time_utc = pytz.utc.localize(current_time)
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    T = current_time_utc.astimezone(beijing_timezone)

    admin_info.objects.all().delete()
    user_info.objects.all().delete()
    Sp_table.objects.all().delete()
    Target_set.objects.all().delete()
    community.objects.all().delete()
    activity.objects.all().delete()
    images.objects.all().delete()
    
    user_info.objects.create(user_name = '1',
                             user_mail = '1@1.cn',
                             user_password = '123456789',
                             user_uid = 11181111,
                             user_academy = id2fac(11181111),
                             user_gender = True,
                             user_time_a = 0,
                             user_num = 0,
                             user_sp_num = 0,
                             user_rtime = T,)

    admin_info.objects.create(user_name = 'admin0',
                              user_mail = '21182645@buaa.edu.cn',
                              user_password = '12345678',
                              user_uid = 21182645,
                              user_academy = 0,
                              user_num = 0,
                              )
    for i in range(1,47) :
        admin_info.objects.create(user_name = 'admin'+ str(i),
                                  user_mail = '0000'+str(i)+'@buaa.edu.cn',
                                  user_password = '123456789',
                                  user_uid = 21000000+i*10000,
                                  user_academy = id2fac(21000000+i*10000),
                                  user_num = i,
                                  )
    for i in range (2,11) :
        user_info.objects.create( user_name = str(i),
                                  user_mail = str(i)+'@'+str(i)+'.edu.cn',
                                  user_password = '123456789',
                                  user_uid = 11000000+i*10000,
                                  user_academy = id2fac(11000000+i*10000),
                                  user_gender = True,
                                  user_time_a = i,
                                  user_num = i,
                                  user_sp_num = i,
                                  user_rtime = T
                                )    

    return HttpResponse('delete success')


def add(request):
    Sp_table.objects.all().delete()          

    return HttpResponse('delete success')


num2sp = {1:'跑步',
          2:'足球',
          3:'排球',
          4:'游泳',
          5:'篮球',
          6:'羽毛球',
          7:'骑行',
          8:'健身',
          9:'登山',
          10:'乒乓球',
          11:'其他'}


num2fac={0:'0号学院',
         1:'材料科学与工程学院',
         2:'电子信息工程学院',
         3:'自动化科学与电气工程学院',
         4:'能源与动力工程学院',
         5:'航空科学与工程学院',
         6:'计算机学院',
         7:'机械工程及自动化学院',
         8:'经济管理学院',
         9:'数学科学学院',
         10:'生物工程学院',
         11:'人文社会科学学院',
         12:'外国语学院',
         13:'交通科学与工程学院',
         14:'可靠性与系统工程学院',
         15:'宇航学院',
         16:'飞行学院',
         17:'仪器科学与光电工程学院',
         18:'北京学院',
         19:'物理学院',
         20:'法学院',
         21:'软件学院',
         22:'继续教育学院',
         23:'高等理工学院',
         24:'中法工程学院',
         25:'国际学院',
         26:'新媒体艺术与设计学院',
         27:'化学学院',
         28:'马克思主义学院',
         29:'人文与社会科学高等研究院',
         30:'空间与环境学院',
         31:'无人系统研究院',
         32:'航空发动机研究院',
         33:'体育部',
         34:'北海学院',
         35:'国际通用工程学院',
         36:'国际交叉科学研究院',
         37:'北航学院',
         38:'医学院',
         39:'网络空间安全学院',
         40:'医工交叉创新研究院',
         41:'微电子学院',
         42:'人工智能研究院',
         43:'前沿科学技术创新研究院',
         44:'大学数据科学与脑机智能高精尖创新中心',
         45:'经济学与商学研究院',
         46:'高等教育研究院'}


def id2fac(id):
    return (int(id)/10000)%100


def generate_verification_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


@csrf_exempt    #发验证邮件
def send_verification_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        # print(email)

        if user_info.objects.filter(user_mail=email).exists():
            return JsonResponse({"error": "该邮箱已经注册过了，请尝试其他邮箱。"}, status=400)

        verification_code = generate_verification_code()
        # 更新验证码存储到Django的缓存中，设置过期时间为10分钟
        cache.set(email, verification_code, timeout=600)

        send_mail(
            '注册验证码',
            f'您的验证码是：{verification_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return JsonResponse({"message": "验证码已发送，请查收邮件。"}, status=200)
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=400)


@csrf_exempt    #注册
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # print(data)
        email = data.get("email")
        input_code = data.get("code")
        password = data.get("password")
        username = data.get("username")
        userid = data.get("userid")
        # 从Django的缓存中获取验证码
        # correct_code = cache.get(email)
        # if not correct_code or input_code != correct_code:
        #     return JsonResponse({"error": "验证码错误或已过期。"}, status=400)
        print(f"Received data: email={email}, code={input_code}, password={password}, userid={userid}")
            # 从Django的缓存中获取验证码
        correct_code = cache.get(email)
        print(f"Correct code from cache: {correct_code}")

        if not correct_code or input_code != correct_code:
            return JsonResponse({"error": "验证码错误或已过期。"}, status=400)

        # password_hash = hashlib.sha256(password.encode()).hexdigest()
        # User.objects.create(email=email, password_hash=password_hash)
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        print(f"Generated password hash: {password_hash}")
        useracademy = int(id2fac(int(userid)))
        user_info.objects.create(user_name = username,
                                 user_mail = email, 
                                 user_password = password,
                                 user_uid = userid,
                                 user_academy = useracademy)
        
        print("User created successfully.")

        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        user_info.objects.filter(user_mail = email).update(user_rtime = i)

        return JsonResponse({"message": "注册成功。"}, status = 200)
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #登录
def Login(request):
    if request.method == 'POST' :
        data = json.loads(request.body)
        # print(data)
        usermail = data.get("email")
        # userid = ('username')
        password = data.get("password")
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        print(usermail,password)

        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)

        if not all([usermail,password]):
            return JsonResponse({"message": "请填写用户名和密码.", 'status':'400'},status=400)

        #超级管理员
        if usermail == '+-*/':
            if password == '+-*/':
                return JsonResponse({"message": "超级管理员登陆成功.",'status':'success'}, status=200)
               
        #管理端判断
        if admin_info.objects.filter(user_mail = usermail).exists():
            admin = admin_info.objects.filter(user_mail = usermail).first()
            if admin.user_password != password :
                return JsonResponse({"message": "密码错误，请重试.",'status':'400'}, status=400)
            return JsonResponse({"message": "管理员登陆成功.",'number':admin.user_academy,'status':'success'}, status=200)

        #用户
        if user_info.objects.filter(user_mail = usermail).exists() == False:
            return JsonResponse({"message": "该用户未注册.",'status':'400'},status=400)

        user = user_info.objects.filter(user_mail = usermail).first()

        if user.user_lock == True :
            time_d = i - user.user_last_login_error 
            # print(time_d.total_seconds())
            if time_d.total_seconds() > 300:
                user_info.objects.filter(user_mail = usermail).update(user_lock = False)
                user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = 0)
                if user.user_password != password :
                    user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = 1)
                    user_info.objects.filter(user_mail = usermail).update(user_last_login_error = i)
                    user_info.objects.filter(user_mail = usermail).update(user_lock = 0)
                    return JsonResponse({"message": "密码错误",'status':'400'},status=400)
                else :
                    user_info.objects.filter(user_mail = usermail).update(user_last_login = i)
                    user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = 0)
                    user_info.objects.filter(user_mail = usermail).update(user_lock = 0)
                    return JsonResponse({"message":"登陆成功.",'number':user.user_academy,'status':'success'},status=200)
            return JsonResponse({"message": "该用户已冻结，请稍后再试.",'status':'400'},status=400)
        
        if user.user_password != password :
            pass_errnum = user.user_pass_errnum
            user_info.objects.filter(user_mail = usermail).update(user_last_login_error = i)
            if pass_errnum >= 400000 :
                user_info.objects.filter(user_mail = usermail).update(user_lock = True)
                user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = 0) 
                return JsonResponse({"message": "该用户已冻结,请5分钟后再试.",'status':'400'},status=400)
            pass_errnum += 1; 
            user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = pass_errnum)
            return JsonResponse({"message": "密码错误，请重试.",'status':'400'}, status=400)
        
        request.session['usermail'] = usermail
        user_info.objects.filter(user_mail = usermail).update(user_last_login = i)
        user_info.objects.filter(user_mail = usermail).update(user_pass_errnum = 0)
        return JsonResponse({"message":"登陆成功.",'number':user.user_academy,'status':'success'}, status=200)
    
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #打卡
def Sp_submisson(request) :
    # usermail = request.session.get('usermail')
    # print(usermail)
    # # usermail = '21182619@buaa.edu.cn'
    if request.method == 'POST' :
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        # iyaer = i-timedelta()
        current_year = i.year
        
        data = json.loads(request.body)
        usermail = data.get('usermail')
        usern = user_info.objects.filter(user_mail = usermail).first()

        sptimebegin = data.get('date')
        sptime = data.get('time')
        sptype = data.get('type')
        splocation = data.get('position')
        spimage = data.get('message')
        # print(spimage)
        sptype = num2sp[int(sptype)]

        spimage_dict = spimage[0]
        spimage_url = spimage_dict.get('url')
        
        print('1')
        print(spimage_url)

        url_data = json.loads(spimage_url)

        url = url_data.get('url')
        print(url)
        file_name = str(url).split('/')[-1]

        print(file_name)
        print('1')

        print(usermail, sptimebegin, sptime, sptype, splocation,spimage_url)

        # image_file = request.FILES.get('file')  # 获取上传的文件对象
        

        # if not all([sptimebegin,sptime,sptype,splocation]):
        #     return JsonResponse({"error": "请填写完整."}, status=400)        
        #create id
        latest_sp_id = Sp_table.objects.all().order_by('-pk').first()
        if latest_sp_id :
            spid = latest_sp_id.sp_id
            spid+=1
        else :
            spid = 1

        latest_sp_pid = Sp_table.objects.filter(user_mail = usermail).order_by('-pk').first()
        if latest_sp_pid :
            sppid = latest_sp_pid.sp_pid
            sppid+=1
        else :
            sppid = 1

        #load image
        # img_temp = BytesIO()
        # img_temp.write(urlretrieve(spmessage[0]['tempFilePath'])[0])
        # img_temp.seek(0)

        # img = Image.open(img_temp)

        date_format = "%m/%d"
        sptimebegin = datetime.strptime(sptimebegin, date_format)

        if sptimebegin > datetime.now() - timedelta(days=30):
            year = current_year + 1
        else:
            year = current_year
        
        print(year)
        new_sptimebegin = sptimebegin.date().replace(year=year)

        print(new_sptimebegin.year)

        new = Sp_table.objects.create(user_name = usern.user_name,
                                user_mail = usermail,
                                user_uid = usern.user_uid,
                                sp_time_begin = new_sptimebegin,
                                sp_time_end = new_sptimebegin + timedelta(minutes=int(sptime)),
                                sp_time = sptime,
                                sp_type = sptype,
                                sp_date = i,
                                sp_location = splocation,
                                file_name = file_name,
                                sp_message = file_name,
                                sp_pid=sppid,
                                sp_id = spid,
                                sp_love_n = 0
                                )
        

        # if image_file:
        #     # 读取图片内容
        #     image_content = image_file.read()
            
        #     # 创建模型实例并保存到数据库
        #     # your_model_instance = Sp_table.objects.filter(user_mail = usermail).first()
        #     new.sp_image.save(image_file.name, ContentFile(image_content), save=True)

        user = user_info.objects.filter(user_mail = usermail)
        user.update(user_sp_num = sppid)
        user.update(user_time_a = user.first().user_time_a + int(sptime))

        return JsonResponse({"message":"打卡成功."},status = 200)

    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)    


@csrf_exempt    #打卡显示
def Sp_sub_show(request) :
    # usermail = request.session.get('usermail')
    # print(usermail)
    if request.method == 'POST' :
        data = json.loads(request.body)
        spid = data.get('sp_id')
        print(spid)

        Spsub_for1_data = []
        Spsub_for1 = Sp_table.objects.filter(sp_id = spid)
        for sp in Spsub_for1:
            # sp.sp_message = os.path.join(ngrok,sp.file_name)
            # sp.sp_message = sp.sp_message + '/'
            # headers = {
            #     'ngrok-skip-browser-warning': 'true'  # 设置ngrok-skip-browser-warning请求头
            # }
            # sp.sp_message = requests.get(sp.sp_message, headers=headers)
            file_name = sp.file_name
            image_url = images.objects.filter(file_name=file_name).first().image_url
            sp.sp_message = image_url
            print(image_url)
            print(sp.sp_message)
            sp.save()

        Spsub_for1_data = list(Spsub_for1.values())
        print(Spsub_for1_data)

        return JsonResponse({'data':Spsub_for1_data})

    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #目标设定
def Tar_set(request) :
    # usermail = request.session.get('usermail')
    # print(usermail)
    # usermail = '21182619@buaa.edu.cn'
    if request.method == 'POST' :
        data = json.loads(request.body)
        usermail = data.get('usermail')
        tsaim_time = data.get('time')
        tstype = data.get('type')
        tsremind = data.get('remind')
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)

        print(usermail,tsaim_time,tstype,tsremind)
        tsaim_time = int(tsaim_time) /1000
        tsaim_time = datetime.fromtimestamp(tsaim_time)  # 将毫秒转换为秒
        tsaim_time = tsaim_time.strftime('%Y-%m-%d %H:%M:%S')
        tstype = num2sp[int(tstype)]

        print(usermail,tsaim_time,tstype,tsremind)

        if not all([tsaim_time,tstype]):
            return JsonResponse({"error": "请填写完整."}, status=400)
        
        latest_aim_pid = Target_set.objects.filter(user_mail = usermail).order_by('-pk').first()
        if latest_aim_pid :
            aimid = latest_aim_pid.ts_aim
            aimid+=1
        else :
            aimid = 1


        Target_set.objects.create(user_mail = usermail, 
                                  ts_aim = aimid, 
                                  ts_aim_time = tsaim_time, 
                                  ts_type = tstype, 
                                  ts_remind = tsremind,
                                  ts_reminded = False
                                 )
        
        return JsonResponse({"message":"目标设定成功."})

    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)  
    

@csrf_exempt    #目标显示
def Tar_set_show(request) :
    # usermail = request.session.get('usermail')
    # print(usermail)
    if request.method == 'POST' :
        data = json.loads(request.body)
        usermail = data.get('usermail')
        print(usermail)

        tsset_for1 = Target_set.objects.filter(user_mail = usermail)
        tsset_for1_list = list(tsset_for1.values())
        print(tsset_for1_list)
        
        return JsonResponse({'data':tsset_for1_list})

    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #个人数据分析
def Sp_DatanFor1(request) :
    # usermail = request.session.get('usermail')
    # print(usermail)
    # usermail = '21182619@buaa.edu.cn'
    if request.method == 'POST' :
        datain = json.loads(request.body)
        usermail = datain.get('usermail')
        print(usermail)
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        now = i.date()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        user_spdataA = Sp_table.objects.filter(user_mail = usermail)
        user_spdataW = Sp_table.objects.filter(user_mail = usermail,sp_date__range=[start_of_week, end_of_week])

        querysetA = user_spdataA.values('sp_type').annotate(count = Count('sp_type')).order_by('-count')
        if querysetA.exists():
            type_all = querysetA.first()['sp_type']
            querysetW = user_spdataW.values('sp_type').annotate(count=Count('sp_type')).order_by('-count')
            if querysetW.exists():
                type_week = querysetW.first()['sp_type']
            else:
                type_week = 'none'
        else:
            type_all = 'none'

        print(type_all,type_week)

        time_all = 0
        for user_all in user_spdataA:
            time_all = user_all.sp_time + time_all
        time_week = 0
        for user_week in user_spdataW:
            time_week = user_week.sp_time + time_week            
        
        print(time_all,time_week)

        user = user_info.objects.filter(user_mail=usermail).first()
        print(user.user_sp_num)
        print('1')
        #总平均打卡时间
        if int(user.user_sp_num) > 0 :
            avetime = time_all / int(user.user_sp_num)
        else :
            avetime = 0

        print(avetime)
        #排名情况
        alluser = user_info.objects.count()
        rank = (user.user_rank / alluser ) * 100
        print(rank)
        #平均能量消耗
        cal = avetime / 60 * 650 #卡路里
        print(cal)
        
        dataout = {
            'username': user_info.objects.filter(user_mail = usermail).first().user_name,
            'time_all': str(time_all),
            'type_all': str(type_all),
            'time_week': str(time_week),
            'type_week': str(type_week),
            'userspnum': str(user.user_sp_num),
            'average_time': str(avetime),
            'rank': str(int(100-rank)),
            'cal': str(cal),
        }
        print(dataout)
        return JsonResponse({'data': dataout})

    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)         


@csrf_exempt    #重置密码
def send_reset_password_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        userid = data.get("id")

        if not user_info.objects.filter(user_mail = email).exists():
            return JsonResponse({"error": "该邮箱未注册，请检查邮箱是否正确。"}, status=400)

        if not user_info.objects.filter(user_uid = userid).exists():
            return JsonResponse({"error": "该学号未注册，请检查学号是否正确。"}, status=400)

        verification_code = generate_verification_code()
        # 更新验证码存储到Django的缓存中，设置过期时间为10分钟
        cache.set(f"reset_{email}", verification_code, timeout=600)

        send_mail(
            '重置密码验证码',
            f'您的验证码是：{verification_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return JsonResponse({"message": "验证码已发送，请查收邮件。"}, status=200)
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=400)


@csrf_exempt    #重置密码
def reset_password(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        input_code = data.get("code")
        new_password1 = data.get("password1")
        new_password2 = data.get("password2")

        # 检查两次输入的新密码是否一致
        if new_password1 != new_password2:
            return JsonResponse({"error": "两次输入的新密码不一致，请重新输入。"}, status=400)

        correct_code = cache.get(f"reset_{email}")
        if not correct_code or input_code != correct_code:
            return JsonResponse({"error": "验证码错误或已过期。"}, status=400)

        # 如果验证码正确，且两次新密码一致，则更新密码
        user = user_info.objects.get(user_mail=email)
        # user.user_password = hashlib.sha256(new_password1.encode()).hexdigest()
        user.user_password = new_password1
        user.save()

        return JsonResponse({"message": "密码重置成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #查看打卡
def check_user_programme(request):
    if request.method == "POST":
        data = json.loads(request.body)
        useremail = data.get("usermail")
        print(useremail)
        #在数据库中找到信息
        user_programme = Sp_table.objects.filter(user_mail=useremail)
        for sp in user_programme:
            # sp.sp_message = os.path.join(ngrok,sp.file_name)
            # sp.sp_message = sp.sp_message + '/'
            # headers = {
            #     'ngrok-skip-browser-warning': 'true',  # 设置ngrok-skip-browser-warning请求头
            #     'User-Agent': 'My Custom User Agent',
            # }
            # # sp.sp_message = requests.get(sp.sp_message, headers=headers)
            # query_string = urlencode(headers)
            
            # sp.sp_message = f'{sp.sp_message}?{query_string}'
            file_name = sp.file_name
            image_url = images.objects.filter(file_name=file_name).first().image_url
            sp.sp_message = image_url
            print(image_url)
            print(sp.sp_message)

            sp.save()
        user_programmes_list = list(user_programme.values())
        print(user_programmes_list)
        return JsonResponse({"data": user_programmes_list})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #删除打卡
def delete_user_programme(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # username = data.get("username")
        # usermail = data.get("usermail")
        sp_id = data.get("sp_id")
        print(sp_id)
        #在数据库中找到信息并删除
        if Sp_table.objects.filter(sp_id=sp_id).exists() :
            Sp_table.objects.filter(sp_id=sp_id).first().delete()
        return JsonResponse({"message": "删除信息成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #删除用户
def delete_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usermail = data.get('user_uid')
        print('1')
        print(usermail)
        #在数据库中找到并删除
        if user_info.objects.filter(user_uid=usermail).exists():
            user_info.objects.filter(user_uid=usermail).delete()
        return JsonResponse({"message": "删除成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #重置用户密码
def remake_user_password(request):
    if request.method == "POST":
        data = json.loads(request.body)
        useremail = data.get("useremail")
        #在数据库中找到并更新密码
        new_password = user_info.objects.filter(user_mail=useremail).first()
        new_password.user_password = "12345678"
        new_password.save()
        return JsonResponse({"message": "重置密码成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #查看目标
def check_user_target(request):
    if request.method == "POST":
        data = json.loads(request.body)
        useremail = data.get("useremail")
        #在数据库中找到信息
        user_programme = Target_set.objects.filter(user_mail=useremail)
        user_programmes_list = list(user_programme.values())
        return JsonResponse({"data": user_programmes_list})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #删除目标
def delete_user_target(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usermail = data.get("useremail")
        ts_id = data.get("ts_id")
        #在数据库中找到信息并删除
        Target_set.objects.get(user_email = usermail,ts_aim=ts_id).delete()
        return JsonResponse({"message": "删除信息成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #管理端用户信息查询
def check_user_information(request):
    if request.method == "POST":
        data = json.loads(request.body)
        uid = data.get("user_uid")
        #在数据库中找到信息
        user_information = user_info.objects.filter(user_uid=uid).values()

        user_information_list = list(user_information)
        print(user_information_list)
        return JsonResponse({"data": user_information_list})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #管理all用户信息查询
def check_all_user(request):
    #print("111")
    #print(request)
    if request.method == "POST":
        #在数据库中找到信息
        # department_number = request.META.get('HTTP_DEPARTMENT_NUMBER', '')
        # print(department_number)
        data = json.loads(request.body)
        number = data.get('user_academy')
        print(number)
        if int(number) == 0 :
            admin = admin_info.objects.all()
            admin_data = list(admin.values())
            user_information = user_info.objects.all()
            user_information_list = list(user_information.values())
            print(user_information_list)
            return JsonResponse({"data":user_information_list})
        
        user_information = user_info.objects.filter(user_academy = number)
        user_information_list = list(user_information.values())
        #print(user_information)
        print(user_information_list)
        
        return JsonResponse({"data": user_information_list})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt    #用户信息上传修改
def user_info_update(request) :
    if request.method == 'POST' :
        data = json.loads(request.body)
        usermail=data.get('usermail')
        print(usermail)
        name=data.get('username')
        gender=data.get('gender')
        user_info.objects.filter(user_mail=usermail).update(user_name=name,user_gender=gender)
        return JsonResponse({"message": "修改成功。"})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #用户信息显示
def user_info_show(request) :
    if request.method == 'POST' :
        data = json.loads(request.body)
        usermail = data.get("usermail")
        print(usermail)
        # usermail = request.session.get('usermail')
        user = user_info.objects.filter(user_mail=usermail).first()
        return JsonResponse({"User_email": user.user_mail,
                             "User_name":user.user_name,
                             "Uid":user.user_uid,
                             "Gender":user.user_gender,
                             "Time_a":user.user_time_a,
                             'Num':user.user_num
                            })
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #用户注销
def user_info_logout(request) :
    if request.method == 'POST' :
        data = json.loads(request.body)
        usermail = data.get("useremail")
        user_info.objects.get(user_mail=usermail).delete()
        return JsonResponse({"message": "删除成功。"})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #用户排名
def user_info_urank(request) :
    if request.method == 'POST' :
        data = json.loads(request.body)
        # usermail = data.get("useremail")
        user_rankings = user_info.objects.order_by('user_rank')[:10]
        user_rankings_list = list(user_rankings.values())
        print(user_rankings_list)
        return JsonResponse({'data': user_rankings_list})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #管理员数据管理
def admin_user(request):
    if request.method == 'POST':
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        now = i.date()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        ytd = now - timedelta(days=1)

        #昨天
        new_ytd = user_info.objects.filter(user_rtime__range=[ytd, now])
        #本周
        new_wk = user_info.objects.filter(user_rtime__range=[start_of_week, end_of_week])

        new_num_ytd = new_ytd.count() #昨日新用户数量
        new_num_wk = new_wk.count() #一周新用户数量


        print(new_num_ytd,new_num_wk)
        return JsonResponse()


@csrf_exempt    #查看管理员信息
def admin_inf(request):
    if request.method == 'POST' :
        data = json.loads(request.body)
        admin = admin_info.objects.all()
        admin_data = list(admin.values())
        print(admin_data)
        return JsonResponse({"data": admin_data})
    

@csrf_exempt    #删除管理员
def delete_admin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mail=data.get('adminmail')
        admin_info.objects.get(user_mail = mail).delete()
        return JsonResponse({"message":"删除成功.",'status':'success'}, status=200)


@csrf_exempt    #打卡举报
def sp_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # uid=data.get('userid')
        pid=data.get('pid')
        U=Sp_table.objects.filter(sp_id=pid).first()
        U.sp_report=True
        U.save()
        return JsonResponse({"message": "举报成功."})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #评论举报
def com_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comid = data.get('comid')
        print(comid)
        U = community.objects.filter(Com_id=comid).first()
        U.com_report = True
        U.save()
        return JsonResponse({"message": "举报成功."})
    elif request.method == 'OPTIONS':
            # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt  # 返回举报内容
def com_return(request):
    if request.method == 'POST':

        SP=Sp_table.objects.filter(sp_report=True)
        res = list(SP.values())
        COM=community.objects.filter(com_report=True)
        resc = list(COM.values())
        print("resp",res,"recom",resc)
        return JsonResponse({"resp": res,"recom": resc})
    
    elif request.method == 'OPTIONS':
            # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt  # 打卡通过
def sp_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pid = data.get('sp_id')
        U = Sp_table.objects.filter(sp_pid=pid).first()
        U.sp_report=False
        U.save()
        return JsonResponse({'message':'审核通过'})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)
    

@csrf_exempt  # 评论通过
def com_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comid = data.get('comid')
        print(comid)
        U = community.objects.filter(Com_id=comid).first()
        print(U)
        U.com_report = False
        U.save()
        return JsonResponse({'message':'审核通过'})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'  # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)
    

@csrf_exempt  # 所有打卡信息获取
def all_sport(request):
    all_user_sports = Sp_table.objects.all()
    for sp in all_user_sports:
            # sp.sp_message = os.path.join(ngrok,sp.file_name)
            # sp.sp_message = sp.sp_message + '/'
            # print(sp.sp_message)
            # headers = {
            #     'ngrok-skip-browser-warning': 'true',  # 设置ngrok-skip-browser-warning请求头
            #     'User-Agent': 'My Custom User Agent',
            # }
            # query_string = urlencode(headers)
            
            # sp.sp_message = f'{sp.sp_message}?{query_string}'
            # print(sp.sp_message)
            file_name = sp.file_name
            image_url = images.objects.filter(file_name=file_name).first().image_url
            sp.sp_message = image_url
            print(image_url)
            sp.save()

    user_sports_list = list(all_user_sports.values())
    print(user_sports_list)
    return JsonResponse({"data": user_sports_list})


@csrf_exempt #点赞
def sport_love(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_love = data.get('user_love')
        pid = data.get('pid')
        love = Sp_table.objects.filter(sp_id = pid).first()
        love.sp_love_n = love.sp_love_n + 1
        love.save()
        return JsonResponse({"message": "点赞成功.",'likecounts':love.sp_love_n})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)


@csrf_exempt #评论
def sport_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = data.get('comment')
        user_mail = data.get('user_mail')
        spid = data.get('sp_id')
        re_id = data.get('re_id')
        com_user = user_info.objects.filter(user_mail=user_mail).first().user_name

        print(comment,user_mail,spid,re_id,com_user)

        if re_id == 0:
            is_re = 0  
            re_user = ""   
        else :
            is_re = 1
            re_user_mail = community.objects.filter(Com_id = re_id).first().user_mail
            re_user = user_info.objects.filter(user_mail = re_user_mail).first().user_name           

        latest_comid = community.objects.all().order_by('-pk').first()
        if latest_comid :
            comid = latest_comid.Com_id
            comid+=1
        else :
            comid = 1
            com_id = comid

        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        
        print(spid,comment,com_user,is_re,re_id,comid,user_mail,i,re_user,com_user)

        community.objects.create(sp_id=spid,
                                 Comment=comment,
                                 com_username=re_user,
                                 is_re=is_re,
                                 Re_id=re_id,
                                 Com_id=comid, #
                                 user_mail = user_mail,
                                 time = i,
                                 com_user = com_user)
        
        return JsonResponse({"message": "评论成功.",'com_user': com_user,'re_user':re_user})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405) 


@csrf_exempt    # 活动管理
def activity_manage(request):
    if request.method == 'POST':
        res=[]
        act=activity.objects.all()
        for a in act:
            res.append({'act_name':a.act_name,
                        'act_image':a.act_image,})
        return JsonResponse(res)
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    # 活动删除
def activity_del(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        actid=data.get('actid')
        activity.objects.filter(act_id=actid).first().delete()
        return JsonResponse({"message": "删除成功."})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #新用户数据
def admin_user_new(request):
    if request.method == 'POST':
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        now = i.date()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        ytd = now - timedelta(days=1)
        start_of_month = now - timedelta(days=now.month)
        end_of_month = now - timedelta(days=30)
        #昨天
        new_ytd = user_info.objects.filter(user_rtime__range=[ytd, now])
        #本周
        new_wk = user_info.objects.filter(user_rtime__range=[start_of_week, end_of_week])
        #本月
        new_mth = user_info.objects.filter(user_rtime__range=[start_of_month, end_of_month])
        new_num_ytd = new_ytd.count() #昨日新用户数量
        new_num_wk = new_wk.count() #一周新用户数量
        new_num_mth = new_mth.count()#一月新用户数量

        print("yesterday",new_num_ytd, "week",new_num_wk, "month",new_num_mth)
        return JsonResponse({"yesterday":new_num_ytd,
                             "week":new_num_wk,
                             "month":new_num_mth})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)
    

@csrf_exempt    #用户打卡前五
def admin_user_top_five_users(request):
    if request.method == 'POST':
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        now = i.date()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        start_of_month = now - timedelta(days=30)
        end_of_month = start_of_week + timedelta(days=30)

        top_five_users_w = Sp_table.objects.filter(sp_date__range=[start_of_week, end_of_week]) \
                             .values('user_uid') \
                             .annotate(total_check_ins=Count('user_uid')) \
                             .order_by('-total_check_ins')[:5]#周打卡前五用户
        top_five_users_m = Sp_table.objects.filter(sp_date__range=[start_of_month, end_of_month]) \
                               .values('user_uid') \
                               .annotate(total_check_ins=Count('user_uid')) \
                               .order_by('-total_check_ins')[:5]#月打卡前五用户
        week=[]
        month=[]
        print(top_five_users_w)

        for i in top_five_users_w:
            week.append({'studentId':i['user_uid'],"department":num2fac[int(id2fac(i['user_uid']))],"checkInCount":i['total_check_ins']})
        for i in top_five_users_m:
            month.append({'studentId':i['user_uid'],"department":num2fac[int(id2fac(i['user_uid']))],"checkInCount":i['total_check_ins']})
        print("week",week,"month",month)

        return JsonResponse({"week":week,"month":month})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)    
    

@csrf_exempt    #运动前五
def admin_user_top_five_sports(request):
    if request.method == 'POST':
        #time
        current_time = datetime.now()
        current_time_utc = pytz.utc.localize(current_time)
        beijing_timezone = pytz.timezone('Asia/Shanghai')
        i = current_time_utc.astimezone(beijing_timezone)
        now = i.date()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        ytd = now - timedelta(days=1)
        start_of_month = now - timedelta(days=30)
        end_of_month = start_of_month + timedelta(days=30)

        top_five_sports_w = Sp_table.objects.filter(sp_date__range=[start_of_week, end_of_week]) \
                               .values('sp_type') \
                               .annotate(total_check_ins=Count('sp_type')) \
                               .order_by('-total_check_ins')[:5]#周运动前五
        top_five_sports_m = Sp_table.objects.filter(sp_date__range=[start_of_month, end_of_month]) \
                               .values('sp_type') \
                               .annotate(total_check_ins=Count('sp_type')) \
                               .order_by('-total_check_ins')[:5]#月运动前五
        week = []
        month = []
        for i in top_five_sports_w:
            week.append({"sport":i['sp_type'],"checkInCount":i['total_check_ins']})
        for i in top_five_sports_m:
            month.append({"sport":i['sp_type'],"checkInCount":i['total_check_ins']})
        
        print("week", week, "month", month)
        return JsonResponse({"week": week, "month": month})
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST'
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)
    

@csrf_exempt    # 发布活动
def activity_upload(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        image = data.get('image')

        print(image)
        # spimage_dict = image[0]
        # spimage_url = spimage_dict.get('url')
        
        # print('1')
        # print(spimage_url)

        # url_data = json.loads(spimage_url)

        # url = url_data.get('url')
        # print(url)
        # file_name = str(url).split('/')[-2]

        # print(file_name)

        latest_sp_id = activity.objects.all().order_by('-pk').first()
        if latest_sp_id :
            actid = latest_sp_id.act_id
            actid+=1
        else :
            actid = 1

        print(actid)

        activity.objects.create(act_name=name,
                                act_image=image,
                                act_id = actid
                                )

        return JsonResponse({'message':'发布成功'})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)


@csrf_exempt    #删除评论
def delete_user_com(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Com_id = data.get("Com_id")
        print(Com_id)
        #在数据库中找到信息并删除
        community.objects.filter(Com_id=Com_id).first().delete()
        return JsonResponse({"message": "删除评论成功。"})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)
    

@csrf_exempt    # 活动管理
def activity_manage(request):
    if request.method == 'POST':
        act=activity.objects.all()
        # for sp in act:
        #     sp.act_image = os.path.join(ngrok,sp.file_name)
        #     sp.act_image = sp.act_image + '/'
        #     print(sp.act_image)
        #     sp.save()
        act_list = list(act.values())
        return JsonResponse({'data': act_list})
    
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400)
    

@csrf_exempt    # 评论管理
def com_manage(request):
    if request.mothod == 'POST':
        com=community.objects.all()
        res=[]
        for a in com:
            res.append({'Com_id':a.com_id,
                        'user_id':a.user_id,
                        'user_name':user_info.objects.get(user_uid=a.user_id).user_name,
                        'time':a.time,
                        'Comment':a.Comment})
        return JsonResponse(res)
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400) 


@csrf_exempt #单条运动打卡的所有评论
def sp_com(request) : 
    if request.method == 'POST' :
        data = json.loads(request.body)
        spid = data.get('sp_id')
        print(spid)
        sp_com_all = community.objects.filter(sp_id = spid)
        sp_com_all_list = list(sp_com_all.values())
        return JsonResponse({'data':sp_com_all_list})
    elif request.method == 'OPTIONS':
        # 返回允许的请求方法
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = 'POST' # 设置允许的请求方法
        return response
    else:
        return JsonResponse({"error": "仅支持POST请求."}, status=400) 


@csrf_exempt   
def get_comment(request): #获取本系所有评论
    if request.method == "POST":
        
        data = json.loads(request.body)
        user_academy = data.get('user_academy')
        print(user_academy)
        if not user_academy:
            return JsonResponse({"error": "缺少学院号。"}, status=400)
        if user_academy == '0':
            comments = community.objects.all()
            comments_list = list(comments.values())
            print(comments_list)
            return JsonResponse({"comments": comments_list})
            
        students = user_info.objects.filter(user_academy=user_academy).values('user_mail')
        print(students)
        if not students.exists():
            return JsonResponse({"error": "未找到该学院的学生。"}, status=404)
        emails = [student['user_mail'] for student in students]
        print(emails)
        comments = community.objects.filter(user_mail__in=emails).values()
        print(comments)
        comments_list = list(comments.values())
        print(comments_list)
        return JsonResponse({"comments": comments_list})

    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)        


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        image_file = request.FILES.get('file')  # 获取上传的文件对象
        if image_file:
            # 读取图片内容
            image_content = image_file.read()
            image = Image.open(image_file)
            image.show()
            
            g = Github('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')

            # 获取仓库
            repo = g.get_repo('hiod17/bottle')

            # 创建文件路径
            file_path = 'uploads/' + image_file.name

            # 上传图片文件
            repo.create_file(file_path, 'Upload image', image_file.read())

            # 构建图片地址
            image_url = f'https://github.com/hiod17/bottle/blob/main/{file_path}'
            file_name = image_file.name
            print('上传的文件名:', file_name)          
            # 创建模型实例并保存到数据库
            # your_model_instance = images()
            # your_model_instance.sp_image.save(image_file.name, ContentFile(image_content), save=True)            
            # image_url = request.build_absolute_uri(your_model_instance.sp_image.url)
            # image_url = image_url + '/'            

            print(image_url)
            images.objects.create(file_name = file_name,image_url=image_url)


            return JsonResponse({'data': '成功','url': file_name,'isImage': 'true','deletable': 'true',}, status=200)
    
    return JsonResponse({'error': '请求无效'}, status=400)


@csrf_exempt #取消点赞
def sport_love_cancel(request):
    if request.method == "POST":
        data = json.loads(request.body)
        pid = data.get('pid')
        love = Sp_table.objects.filter(sp_id = pid).first()
        if love.sp_love_n > 0:
            love.sp_love_n = love.sp_love_n - 1
        love.save()
        return JsonResponse({'data': '成功','likecounts':love.sp_love_n})
    else:
        return JsonResponse({"error": "仅支持POST请求。"}, status=405)
    



# @csrf_exempt
# def download(request):
#     # image_relative_path = "/update/uploads/DuhsfffZwwBFa76f8b3879954f4082922f72be870c7f.png"
#     image_path = "./update/uploads/DuhsfffZwwBFa76f8b3879954f4082922f72be870c7f.png"

#     # 获取当前请求的绝对URL
#     absolute_url = request.build_absolute_uri(image_path)

#     # 打印绝对URL
#     print(absolute_url)

#     # 返回一个包含绝对URL的响应
#     with urllib.request.urlopen(absolute_url) as f:
#         image_data = f.read()

#     # 返回图片数据作为响应
#     return HttpResponse(image_data, content_type="image/png")