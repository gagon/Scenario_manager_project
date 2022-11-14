from django.contrib import admin

from .models import Model2, Trends, Events, Scenario


# Register your models here.
@admin.register(Model2)
class Model2Admin(admin.ModelAdmin):
    list_display = [
        "model_name", "model_location","model_file_name","created_date",
        "created_by","description",
        ]
    list_filter = ["created_date"]


@admin.register(Trends)
class TrendsAdmin(admin.ModelAdmin):
    list_display = [
        "trends_name", "trends_file_name","start_date","end_date",
        "created_date","created_by","description",
        ]
    list_filter = ["created_date"]


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = [
        "events_name", "events_file_name","created_date",
        "created_by", "description",
]
    list_filter = ["created_date"]


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = [
        "scenario_name", "created_date","created_by",
        "start_date", "end_date","description", "run_date","run_by",
        "model_id","trends_id","events_id",
]
    list_filter = ["created_date"]