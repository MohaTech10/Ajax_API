from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.generic import TemplateView

# router_generated = routers.DefaultRouter()
# router_generated.register('task', ViewTaskTranslatedIntoJsonFormat)
# router_generated.register("task/<id:id>", TaskDeleteAPIView)
urlpatterns = [
    path('api/', ViewTaskTranslatedIntoJsonFormat.as_view()),
    path('api/create', TaskCreateAPIView.as_view()),
    path('api/<str:pk>', TaskDetailAPIView.as_view()),
    path('api/update/<str:pk>', TaskUpdateAPIView.as_view()),
    path('api/delete/<str:pk>', TaskDeleteAPIView.as_view()),
    path('', TemplateView.as_view(template_name='all_tasks.html'), name='list_task')
]
