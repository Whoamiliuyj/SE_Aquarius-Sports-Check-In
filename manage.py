import os
import sys
import threading
import pytz
from datetime import datetime
from django.db.models import F, Window
from django.db.models.functions import RowNumber
from django.core.management import execute_from_command_line
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.core.mail import send_mail
from django.conf import settings

#调度器
def start_scheduler():
    print("Starting scheduler...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(Tar_reminder, IntervalTrigger(seconds=30))
    scheduler.start()

#目标提醒
def Tar_reminder():
    from app1.models import user_info,Target_set
    

    current_time = datetime .now()
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    current_time_with_tz = beijing_timezone.localize(current_time)
    beijing_time = current_time_with_tz.astimezone(beijing_timezone)
    formatted_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S')
    print("Django Current Time:", formatted_time+'.')

    #排名 user_rank
    records = user_info.objects.annotate(rank=Window(expression=RowNumber(), order_by=F('user_time_a').desc())).order_by('-user_time_a')
    for record in records:
        record.user_rank = record.rank
        record.save()
    print('Reload User Rank.')

    # 进行数据库调用操作
    tar_for1 = Target_set.objects.all()
    if tar_for1.exists():
        for tar in tar_for1 :
            if tar.ts_remind == True :
                if tar.ts_reminded == False :
                    if tar.ts_aim_time > formatted_time :
                        print(tar)
                        send_mail(
                            '提醒通知',
                            '这是一个定时提醒的邮件。',
                            '运动时间到',
                            settings.EMAIL_HOST_USER,
                            [tar.user_mail],
                            fail_silently=False,
                        )
                        print(tar.user_mail,'已发送')
                        Target_set.objects.filter(user_mail = tar.user_mail,ts_aim = tar.ts_aim,ts_type = tar.ts_type).update(ts_reminded = True)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SE_ASCI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 创建并启动定时任务调度器线程
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.start()

    try:
        # 运行Django开发服务器
        execute_from_command_line(sys.argv)
    finally:
        # 等待定时任务调度器线程结束
        scheduler_thread.join()

        # 其他清理代码...


if __name__ == '__main__':
    main()
