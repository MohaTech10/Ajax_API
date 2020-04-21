from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.generic import TemplateView
router_generated = routers.DefaultRouter()
router_generated.register('task', ViewTaskTranslatedIntoJsonFormat)
urlpatterns = [
    path('api/', include(router_generated.urls)),
    path('', TemplateView.as_view(template_name='all_tasks.html'), name='list_task')
]