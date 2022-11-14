from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



# Create your views here.

# Models
@api_view(http_method_names=["GET"]) # Get models,list
@permission_classes([IsAuthenticated])
def list_model2(request:Request):
    model2s = Model2.objects.all()

    serializer = Model2Serializer(instance=model2s, many=True)

    response = {
        "massage":"models",
        "data":serializer.data
    }
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["POST"]) # Create model
@permission_classes([IsAuthenticated])
def create_models(request:Request):
    user = request.user    
    data = request.data
    
    serializer = Model2CreateSerializer(data=data)

    if serializer.is_valid():
        serializer.save(created_by = user)
            
        response = {
            "massage":"Model Created",
            "data":serializer.data
        }            
        return Response(data=response, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["PUT"]) # Update model
@permission_classes([IsAuthenticated])
def update_models(request:Request, model_id:int):
    model2 = get_object_or_404(Model2,pk=model_id)
    data = request.data

    serializer = Model2CreateSerializer(instance=model2, data=data)

    if serializer.is_valid():
        serializer.save()

        response= {
            "message":"Model Update Successfully",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"]) #Delete model
@permission_classes([IsAuthenticated])
def delete_models(request:Request, model_id:int):
    model2 = get_object_or_404(Model2,pk=model_id)

    model2.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


# Trends
@api_view(http_method_names=["GET"]) # Get Trends, list
@permission_classes([IsAuthenticated])
def list_trends(request:Request):
    trends = Trends.objects.all()

    serializer = TrendsSerializer(instance=trends, many=True)

    response = {
        "massage":"trends",
        "data":serializer.data
    }
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["POST"]) # Create trend
@permission_classes([IsAuthenticated])
def create_trends(request:Request):
    user = request.user    
    data = request.data
    
    serializer = TrendsCreateSerializer(data=data)

    if serializer.is_valid():
        serializer.save(created_by = user)
            
        response = {
            "massage":"Trend Created",
            "data":serializer.data
        }            
        return Response(data=response, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["PUT"]) # Uodate trend
@permission_classes([IsAuthenticated])
def update_trends(request:Request, trend_id:int):
    trends = get_object_or_404(Trends,pk=trend_id)
    data = request.data

    serializer = TrendsCreateSerializer(instance=trends, data=data)

    if serializer.is_valid():
        serializer.save()

        response= {
            "message":"Trend Update Successfully",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"]) # Delete trend
@permission_classes([IsAuthenticated])
def delete_trends(request:Request, trend_id:int):
    trends = get_object_or_404(Trends,pk=trend_id)

    trends.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


# Events
@api_view(http_method_names=["GET"]) # Get events,list
@permission_classes([IsAuthenticated])
def list_events(request:Request):
    events = Events.objects.all()

    serializer = EventsSerializer(instance=events, many=True)

    response = {
        "massage":"events",
        "data":serializer.data
    }
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["POST"]) # Create event
@permission_classes([IsAuthenticated])
def create_events(request:Request):
    user = request.user  
    data = request.data
    
    serializer = EventsCreateSerializer(data=data)

    if serializer.is_valid():
        serializer.save(created_by = user)
            
        response = {
            "massage":"Event Created",
            "data":serializer.data
        }            
        return Response(data=response, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["PUT"]) # Update event
@permission_classes([IsAuthenticated])
def update_events(request:Request, event_id:int):
    events = get_object_or_404(Events,pk=event_id)
    data = request.data

    serializer = EventsCreateSerializer(instance=events, data=data)

    if serializer.is_valid():
        serializer.save()

        response= {
            "message":"Event Update Successfully",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"]) # Delete event
@permission_classes([IsAuthenticated])
def delete_events(request:Request, event_id:int):
    events = get_object_or_404(Events,pk=event_id)

    events.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


#Scenario
@api_view(http_method_names=["GET"]) # Get scenario, list
@permission_classes([IsAuthenticated])
def list_scenario(request:Request):
    scenarios = Scenario.objects.all()

    serializer = ScenarioSerializer(instance=scenarios, many=True)

    response = {
        "massage":"scenarios",
        "data":serializer.data
    }
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"]) # Create scenario
@permission_classes([IsAuthenticated])
def create_scenario(request:Request):
    user = request.user    
    data = request.data    
    serializer = ScenarioCreateSerializer(data=data)  

    if serializer.is_valid() and (Scenario.model_id or Scenario.events_id or Scenario.trends_id is True):
        serializer.save(created_by = user)
                    
        response = {
            "massage":"Scenario Created",
            "data":serializer.data
        }                
        return Response(data=response, status=status.HTTP_201_CREATED)
        
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(http_method_names=["PUT"]) # Update scenario
@permission_classes([IsAuthenticated])
def update_scenario(request:Request, scenario_id:int):
    scenario = get_object_or_404(Scenario,pk=scenario_id)

    data = request.data

    serializer = ScenarioCreateSerializer(instance=scenario, data=data)

    if serializer.is_valid():
        serializer.save()

        response= {
            "message":"Scenario Update Successfully",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"]) # Delete scenario
@permission_classes([IsAuthenticated])
def delete_scenario(request:Request, scenario_id:int):
    scenario = get_object_or_404(Scenario,pk=scenario_id)

    scenario.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

