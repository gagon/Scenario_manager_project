from rest_framework import serializers
from .models import Model2, Trends, Events, Scenario


##### Model2
class Model2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Model2
        fields = ["model_id","model_name", "model_location","model_file_name","created_date",
        "created_by","description",]

class Model2CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model2
        fields = ["model_id","model_name", "model_location","model_file_name","created_date",
        "description",]

##### Trends
class TrendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trends
        fields = ["trends_id","trends_name", "trends_file_name","start_date","end_date",
        "created_date","created_by","description",]

class TrendsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trends
        fields = ["trends_id", "trends_name", "trends_file_name","start_date","end_date",
        "created_date","description",]


##### Events
class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ["events_id","events_name", "events_file_name","created_date",
        "created_by", "description",]

class EventsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ["events_id", "events_name", "events_file_name","created_date",
        "description",]


##### Scenario
class ScenarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        fields = ["scenario_id","scenario_name", "created_date","created_by",
        "start_date", "end_date","description","run_date","run_by",
        "model_id","trends_id","events_id",]

class ScenarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        fields = ["scenario_id", "scenario_name", "created_date",
        "start_date", "end_date","description","run_date","run_by",
        "model_id","trends_id","events_id",]