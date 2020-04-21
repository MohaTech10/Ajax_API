from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets

class ViewTaskTranslatedIntoJsonFormat(viewsets.ModelViewSet):
    # so taking each object in that model view it as it's translated
    queryset = Tasks.objects.all().order_by('-id')
    serializer_class = TranslatedTaskApi
