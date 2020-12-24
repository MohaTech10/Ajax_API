from rest_framework.serializers import ModelSerializer
from .models import *
# just to translate the model to Api Format and json of course
class TranslatedCreateUpdateTaskApi(ModelSerializer):
    # Thats True for Create/Update
    class Meta:
        model = Tasks
        # what to show for developers in API page
        fields = ["task_title", "completed"]

# just to translate the model to Api Format and json of course
class TranslatedAllTaskApi(ModelSerializer):
    class Meta:
        model = Tasks
        # what to show for developers in API page
        fields = ['id', "task_title", "completed"]


# if you wanna make the detail Look in the json data difference change
# here
class TranslatedDetailTaskApi(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
