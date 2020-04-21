from rest_framework.serializers import ModelSerializer
from .models import *

# just to translate the model to Api Format and json of course
class TranslatedTaskApi(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
