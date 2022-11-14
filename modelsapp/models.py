from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Model2(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField("Models", max_length = 50)
    model_location = models.CharField("location", max_length = 150)
    model_file_name = models.CharField("Models file", max_length = 50)
    created_date =  models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")

    def __str__(self) -> str:
        return self.model_name

    class Meta:
        ordering = ["-created_date"]


class Trends(models.Model):
    trends_id = models.AutoField(primary_key=True)
    trends_name = models.CharField("Trends", max_length = 50)
    trends_file_name = models.CharField("Trends file", max_length = 150)
    start_date =  models.DateTimeField("Start_date",auto_now_add=False, auto_now=False, blank=True)   
    end_date =  models.DateTimeField("End_date",auto_now_add=False, auto_now=False, blank=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")

    def __str__(self) -> str:
        return self.trends_name

    class Meta:
        ordering = ["-created_date"]

 
class Events(models.Model):
    events_id = models.AutoField(primary_key=True)
    events_name = models.CharField("Events", max_length = 50)
    events_file_name = models.CharField("Events file", max_length = 150)
    created_date =  models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField("Description")

    def __str__(self) -> str:
        return self.events_name

    class Meta:
        ordering = ["-created_date"]


class Scenario(models.Model):
    scenario_id = models.AutoField(primary_key=True)
    scenario_name = models.CharField("Scenario", max_length = 50)
    created_date =  models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='created_by', on_delete=models.PROTECT)
    run_date = models.DateTimeField("Run_date",blank=True, null=True)
    run_by = models.ForeignKey(User,related_name='Run_by', on_delete=models.PROTECT, blank=True, null=True)
    start_date = models.DateTimeField("Start_date",auto_now_add=False, auto_now=False, blank=True) 
    end_date = models.DateTimeField("End_date",auto_now_add=False, auto_now=False, blank=True)
    description = models.TextField("Description")
    model_id = models.ForeignKey(Model2,on_delete=models.CASCADE)
    trends_id = models.ForeignKey(Trends,on_delete=models.CASCADE)
    #scenario_config_id = models.AutoField(primary_key=True,blank=True, null=True)#таймстеп 
    events_id = models.ForeignKey(Events,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.scenario_name

    class Meta:
        ordering = ["-created_date"]