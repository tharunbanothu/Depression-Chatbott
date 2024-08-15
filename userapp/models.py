from django.db import models

# Create your models here.

class UserModel(models.Model):

          user_id = models.AutoField(primary_key=True)
          user_join_date = models.DateField(auto_now_add=True)
          user_name = models.CharField(max_length=100)
          user_email = models.EmailField()
          user_password = models.CharField(max_length=100)
          user_phone = models.BigIntegerField(null=True)
          user_city = models.CharField(max_length=100)
          user_profile = models.ImageField(upload_to='images/',null=True)
          status = models.CharField(max_length=20,default="pending")

          class Meta:
                    db_table = "user_details"

