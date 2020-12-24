from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,  # to delete an object
    ListAPIView,  # to list all objects
    UpdateAPIView,  # to update an object
    RetrieveAPIView  # to show a detail object
)


class TaskCreateAPIView(CreateAPIView):
    queryset = Tasks.objects.all().order_by('-id')
    serializer_class = TranslatedCreateUpdateTaskApi


class ViewTaskTranslatedIntoJsonFormat(ListAPIView):
    queryset = Tasks.objects.all().order_by('-id')
    serializer_class = TranslatedAllTaskApi


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TranslatedDetailTaskApi
    lookup_field = "pk"


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TranslatedCreateUpdateTaskApi
    lookup_field = "pk"


class TaskDeleteAPIView(DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TranslatedDetailTaskApi
    lookup_field = "pk"
