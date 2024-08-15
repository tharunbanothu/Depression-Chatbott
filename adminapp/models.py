from django.db import models
from userapp.models import UserModel
import os


# Create your models here.

class FeedbackModel(models.Model):
          feedback = models.TextField()
          date = models.DateField(auto_now_add=True,null=True)
          user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
          sentiment = models.CharField(max_length=100,null=True)
          

          class Meta:
                    db_table = "user_feedback"


class FiledataModel(models.Model):
          
          data_file = models.FileField(upload_to='files/')
          depressed = models.CharField(max_length=10,null=True)
          Undepressed = models.CharField(max_length=10,null=True)
          class Meta:
                    db_table = "excel_data"