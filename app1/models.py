from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

#管理员
class admin_info(models.Model):
    user_name = models.CharField(max_length = 16) 
    user_mail = models.EmailField()
    user_password = models.CharField(max_length = 300)
    user_academy = models.IntegerField(default = 100) #学院
    # user_gender = models.BooleanField(null = True,blank = True) #性别
    user_uid = models.IntegerField(default=0) #学号
    # user_time_a = models.IntegerField(default=0) #总运动时间
    # user_time_w = models.IntegerField(default=0) #周运动时间
    user_num = models.IntegerField(default=0)

#用户信息
class user_info(models.Model):
    user_name = models.CharField(max_length = 16) 
    user_mail = models.EmailField()
    user_password = models.CharField(max_length = 300)

    user_academy = models.IntegerField(default = 100) #学院

    user_gender = models.BooleanField(null = True,blank = True) #性别
    user_uid = models.IntegerField(default=0) #学号
    user_time_a = models.IntegerField(default=0) #总运动时间
    # user_time_w = models.IntegerField(default=0) #周运动时间
    user_num = models.IntegerField(default=0) #用户序号
    user_sp_num = models.IntegerField(default=0) #用户打卡次数
    user_rank = models.IntegerField(default=1000)

    # 注册时间
    user_rtime = models.DateField(null=True, verbose_name="注册时间", help_text="注册时间")

    # login 信息
    user_last_login = models.DateTimeField(null=True, verbose_name="最后登录时间", help_text="最后登录时间")
    user_pass_errnum = models.IntegerField(default=0, verbose_name="用户密码输入次数", help_text="用户密码输入次数")
    user_last_login_error = models.DateTimeField(null=True, verbose_name="最后登录错误的时间戳", help_text="最后登录错误的时间戳")
    user_lock = models.BooleanField(default=False, verbose_name="锁", help_text="锁")

#打卡
class Sp_table(models.Model):
    user_name = models.CharField(max_length=16,null = True)
    user_mail = models.EmailField()
    user_uid = models.IntegerField(default=0)

    sp_pid = models.IntegerField(default=0) #打卡的序号（对用户）
    sp_id = models.IntegerField(default=0) #打卡序号
    sp_type = models.CharField(max_length=16) #运动类型
    sp_date = models.DateTimeField(null = True) #打卡时间
    sp_time_begin = models.DateTimeField(null = True) #运动开始时间
    sp_time_end = models.DateTimeField(null = True) #运动结束时间
    sp_time = models.IntegerField(default=0) #运动时长
    sp_location = models.CharField(max_length=128) #运动地点
    sp_message = models.CharField(max_length=2000) #运动信息
    file_name = models.CharField(max_length=2000,null = True) #照片文件名
    sp_love_n = models.IntegerField(default=0) #点赞数

    sp_report = models.BooleanField(null = True, default=0)
    sp_Agency = models.BooleanField(null = True, default=0)
    sp_2Agency = models.BooleanField(null = True, default=0)

    sp_image = models.ImageField(upload_to='uploads/', storage=fs) #照片

#目标
class Target_set(models.Model):
    user_mail = models.EmailField()
    user_uid = models.IntegerField(default=0)
    ts_aim = models.IntegerField(default=0) #提醒的序号
    ts_aim_time = models.DateTimeField(null = True) #目标时间
    ts_type = models.CharField(max_length=16) #目标类型
    ts_remind = models.BooleanField(default=False) #是否设置提醒
    ts_reminded = models.BooleanField(default=False) #是否已提醒

#社区
class community(models.Model):
    user_mail = models.EmailField() 
    com_user = models.CharField(max_length=16,null = True) #回复人用户名
    sp_id = models.IntegerField(default=0)
    is_re = models.BooleanField(default=False) #是否为回复其他评论
    Re_id = models.IntegerField(default=0) #回复评论 id
    Com_id = models.IntegerField(default=0) #评论 id
    com_username = models.CharField(max_length=16,null = True) # 被回复人用户名
    Comment = models.CharField(null = True,max_length=128) #评论内容
    time = models.DateField(null = True)
    com_report = models.BooleanField(null = True, default=0)
    com_Agency = models.BooleanField(null = True, default=0)
    com_2Agency = models.BooleanField(null = True, default=0)

    # ...

#活动
class activity(models.Model) :
    act_name = models.CharField(null = True,max_length=128)
    act_image = models.CharField(max_length=2000,null = True)
    act_id = models.IntegerField(default=0)
    act_time = models.DateField(null = True)
    file_name = models.CharField(max_length=2000,null = True) #照片文件名


#图片    
class images(models.Model) :
    sp_image = models.ImageField(upload_to='uploads/', storage=fs) #照片
    sp_id = models.IntegerField(null = True, default=0)
    file_name = models.CharField(max_length=2000,null = True)
    image_url = models.CharField(max_length=2000,null = True)