"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, HttpResponse, redirect
import os
from PIL import Image

from io import BytesIO

from django.urls import path
from django.http import HttpResponse
import os
from django.http import FileResponse

def download_files(request, filename):
    folder_path = "./update/uploads/"
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        print(file_path)
        image = Image.open(file_path)
        # image.show()
        # with open(file_path, 'rb') as f:
        #     file_data = f.read()

        # 创建一个字节流缓冲区
        # image_buffer = BytesIO()
        # # 将图像保存到字节流缓冲区
        # image.save(image_buffer, format=image.format)
        # # 获取图像数据
        # image_data = image_buffer.getvalue()
        # # 关闭字节流缓冲区
        # image_buffer.close()

        # 设置响应的content_type为图像的MIME类型
        
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        return HttpResponse(status=404)


urlpatterns = [
    #/api/
    path('register/', views.register, name='register'), #注册
    path('send_verification_email/', views.send_verification_email, name='send_verification_email'), #
    path('Login/', views.Login, name = '登录Login'), #登录
            
    #用户
    path('send_reset_password_email/', views.send_reset_password_email, name = 'send_reset_password_email'), #
    path('reset_password/', views.reset_password, name = 'reset_password'), #修改密码

    path('check_user_programme/', views.check_user_programme, name = 'check_user_programme'), #查看打卡
    path('delete_user_programme/', views.delete_user_programme, name = 'delete_user_programme'), #删除打卡  
    path('check_user_target/', views.check_user_target, name = 'check_user_target'), #查看目标
    path('delete_user_target/', views.delete_user_target, name = 'delete_user_target'), #删除目标

    path('Sp_submisson/', views.Sp_submisson, name = 'Sp_submisson'), #打卡
    path('Sp_sub_show/', views.Sp_sub_show, name = 'Sp_sub_show'), #打卡显示
    path('Tar_set/', views.Tar_set, name = 'Tar_set'), #目标设定
    path('Tar_set_show/', views.Tar_set_show, name = 'Tar_set_show'), #目标显示
    path('Sp_DatanFor1/', views.Sp_DatanFor1, name = 'Sp_DatanFor1'), #个人数据分析
        
    path('user_info_update/', views.user_info_update, name = 'user_info_update'), #用户信息上传修改
    path('user_info_show/', views.user_info_show, name = 'user_info_show'), #用户信息显示
    path('user_info_logout/', views.user_info_logout, name = 'user_info_logout'), #用户注销
    path('user_info_urank/', views.user_info_urank, name = 'user_info_urank'), #用户注销
    
    path('sp_report/', views.sp_report, name = 'sp_report'), #打卡举报
    path('com_report/', views.com_report, name = 'com_report'), #评论举报
    path('sport_love/', views.sport_love, name = 'sport_love'), #点赞
    path('sport_comment/', views.sport_comment, name = 'sport_comment'), #评论

    #管理
    path('delete_user/', views.delete_user, name = 'delete_user'), #删除用户
    path('remake_user_password/', views.remake_user_password, name = 'remake_user_password'), #重置密码
    path('check_user_information/', views.check_user_information, name = 'check_user_information'), #管理端用户信息查询
    path('check_all_user/', views.check_all_user, name = 'check_all_user'), #管理all用户信息查询
    path('admin_user/', views.admin_user, name = 'admin_user'), #管理员数据管理
    path('admin_inf/', views.admin_inf, name = 'admin_inf'), #查看管理员信息
    path('delete_admin/', views.delete_admin, name = 'delete_admin'), #删除管理员
    path('sp_pass/', views.sp_pass, name = 'sp_pass'), #打卡通过
    path('com_pass/', views.com_pass, name = 'com_pass'), #评论通过
    path('all_sport/', views.all_sport, name = 'all_sport'), #所有打卡信息获取
    path('activity_manage/', views.activity_manage, name = 'activity_manage'), #活动管理
    path('activity_del/', views.activity_del, name = 'activity_del'), #活动删除
    path('com_return/', views.com_return, name = 'com_return'), #返回举报内容

    #new
    path ('sport_love_cancel/',views.sport_love_cancel),#取消点赞

    path ('get_comment/',views.get_comment),#获取本系所有评论

    path ('delete_user_com/',views.delete_user_com), #删除评论
    path ('activity_upload/',views.activity_upload), #发布活动
    path ('sp_com/',views.sp_com), #单条运动打卡的所有评论

    path ('admin_user_new/',views.admin_user_new), #新用户数据
    path ('admin_user_top_five_users/',views.admin_user_top_five_users), #用户打卡前五
    path ('admin_user_top_five_sports/',views.admin_user_top_five_sports), #运动前五

    path ('upload/',views.upload), #图片upload
    # path ('download/',views.download),
    path('download/<str:filename>/', download_files, name='download'),

    path ('delete_data/',views.delete_sql_data), #清空所有表!!!
    #test
    path ('django-mysql-test/',views.django_mysql_test),
    path ('add/',views.add),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)