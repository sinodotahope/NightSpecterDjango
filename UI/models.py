from django.db import models

# Create your models here.
from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=200,verbose_name='作业组成员')
    work_date = models.DateTimeField('作业日期')
    num_workers = models.IntegerField(verbose_name='作业人数')
    def __str__(self):
        return self.group_name


class Tool(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    num_tools = models.IntegerField(verbose_name='工具数量')
    num_materials = models.IntegerField(verbose_name='材料数量')
    def __str__(self):
        return "工具"+str(self.num_tools)+"；材料"+str(self.num_materials)

class Door(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    up_door = models.CharField(max_length=200,verbose_name='上道站台')
    down_door = models.CharField(max_length=200,verbose_name='下道站台')
    def __str__(self):
        return "上道："+str(self.up_door)+"；下道："+str(self.down_door)

