from django.db import models

class HealthInfo(models.Model):
    id = models.AutoField('id',primary_key=True)
    sex = models.CharField('性别',max_length=255,default='')
    age = models.CharField('年龄',max_length=255,default='') #level
    career = models.CharField('职业',max_length=255,default='') #level
    sleep_duration = models.CharField('睡眠时长',max_length=255,default='')  #discount
    sleep_quality = models.CharField('睡眠质量',max_length=255,default='')
    physical_activity_level = models.CharField('身体活动水平',max_length=255,default='') #score
    pressure = models.CharField('压力水平',max_length=255,default='') #price
    bmi = models.CharField('BMI',max_length=255,default='') #price
    blood_pressure = models.CharField('血压',max_length=255,default='') #commentsLen
    heart_rate = models.CharField('心率',max_length=255,default='')
    daily_steps = models.CharField('每日步数',max_length=255,default='')
    sleep_disorders = models.CharField('睡眠障碍',max_length=255,default='')
    comments = models.TextField('用户评论', default='')
    createTime = models.DateField('爬取时间',auto_now_add=True)

    class Meta:
        managed = True
        db_table = "app_health"
        verbose_name_plural = verbose_name = '睡眠健康数据表'    #设置后台显示的名称

    def __str__(self):
        return self.age                       #显示该表的字段


class User(models.Model):
    id = models.AutoField('id',primary_key=True)
    username = models.CharField('用户名',max_length=255,default='')
    password = models.CharField('密码',max_length=255,default='')
    sex = models.CharField('性别',max_length=255,default='')
    phone = models.CharField('电话号码',max_length=255,default='')
    age = models.CharField('年龄',max_length=255,default='')
    career = models.CharField('职业',max_length=255,default='')
    sleep_duration = models.CharField('睡眠时长',max_length=255,default='')
    sleep_quality = models.CharField('睡眠质量',max_length=255,default='')
    physical_activity_level = models.CharField('身体活动水平',max_length=255,default='')
    pressure = models.CharField('压力水平',max_length=255,default='')
    bmi = models.CharField('BMI',max_length=255,default='')
    blood_pressure = models.CharField('血压',max_length=255,default='')
    heart_rate = models.CharField('心率',max_length=255,default='')
    daily_steps = models.CharField('每日步数',max_length=255,default='')
    sleep_disorders = models.CharField('睡眠障碍',max_length=255,default='')
    state = models.CharField('公开状态',max_length=255,default='')
    avatar = models.FileField('头像',upload_to='avatar',default='avatar/default.png')
    textarea = models.CharField('个人简介',max_length=255,default='这个人很懒，什么有没留下。')
    createTime = models.DateField('创建时间',auto_now_add=True)
    comments = models.TextField('用户评论', default='')

    class Meta:
        db_table = "app_user"
        verbose_name_plural = verbose_name = '用户表'  # 设置后台显示的名称

    def __str__(self):
        return self.username  # 显示该表的字段
