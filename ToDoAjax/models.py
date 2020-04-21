from django.db import models

# this is our model so it's inside of Django app we wanna other techs read it
# and deal with and read and write on it and so on, so we have to translate it
# to Json APi format so all other techs would easily read it !
# then we have to view the model cuz it contains all the data and also
# view it after being serialized !
class Tasks(models.Model):
    task_title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
