from . import views
from django.urls import path


urlpatterns = [
    path("model/",views.list_model2, name="list_model2"),
    path("model_create/",views.create_models, name="create_models"),
    path("model_update/<int:model_id>/",views.update_models, name="update_models"),
    path("model_delete/<int:model_id>/",views.delete_models, name="delete_models"),

    path("trend/",views.list_trends, name="list_trends"),
    path("trend_create/",views.create_trends, name="create_trends"),
    path("trend_update/<int:trend_id>/",views.update_trends, name="update_trend"),
    path("trend_delete/<int:trend_id>/",views.delete_trends, name="delete_trend"),

    path("event/",views.list_events, name="list_events"),
    path("event_create/",views.create_events, name="create_events"),
    path("event_update/<int:event_id>/",views.update_events, name="update_event"),
    path("event_delete/<int:event_id>/",views.delete_events, name="delete_event"),


    path("scenario/",views.list_scenario, name="list_scenario"),
    path("scenario_create/",views.create_scenario, name="create_scenario"),
    path("scenario_update/<int:scenario_id>/",views.update_scenario, name="update_scenario"),
    path("scenario_delete/<int:scenario_id>/",views.delete_scenario, name="delete_scenario"),
    
]