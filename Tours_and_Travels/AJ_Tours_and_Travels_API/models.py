from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

class RegisterUser(models.Model):
    phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$',
                                 message="Phone number must be entered in the format: '999999999',0989279999 Up to 14 digits allowed.")
    email_regex = RegexValidator(regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                                 message="Email Id must be entered in the format: example326@gmail.com' Up to 50 character allowed.")

    userId = models.IntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(validators=[email_regex], max_length=500, null=True)
    password = models.CharField(max_length=20, null=True)
    profile_image = models.FileField(null=True, upload_to='images/profile_images/')
    mob_no = models.CharField(validators=[phone_regex], max_length=15, null=True)
    OTP = models.IntegerField(null=True)
    fb_check = models.CharField(max_length=500, null=True)
    loc_latitude = models.FloatField(null=True)
    loc_longitude = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if self.pk is None:
            self.created_at = timezone.now()
            usr_name = self.email
            print(usr_name)
            user_obj = User.objects.create_user(
                username=usr_name, password=self.password, is_staff=False, email=self.email,
                first_name=self.first_name, last_name=self.last_name
            )
            user_data = list(User.objects.filter(username=user_obj).values('pk'))
            user_data[0].get('pk')
            print(user_data[0].get('pk'))
            self.userId = user_data[0].get('pk')
            self.user_id = user_data[0].get('pk')
            res = super(RegisterUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        else:
            self.updated_at = timezone.now()
            res = super(RegisterUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        return res

class Car_Reservation(models.Model):
    Select_your_car = models.CharField(null=False, blank=True, max_length=200)
    Pick_up_City = models.CharField(null=False, blank=True, max_length=200)
    Drop_off_City = models.CharField(null=True, blank=True, max_length=200)
    Pick_up_DateTime = models.DateTimeField(null=False, blank=True)
    Drop_off_DateTime = models.DateTimeField(null=True, blank=True)
   
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Select_your_car
    
class Send_Your_Message(models.Model):
    Name = models.CharField(null=False, blank=True, max_length=200)
    Email = models.EmailField(null=False, blank=True, max_length=200)
    Phone = models.IntegerField()
    Project = models.CharField(null=False, blank=True, max_length=200)
    Subject = models.CharField(null=False, blank=True, max_length=200)
    Massage = models.CharField(null=False, blank=True, max_length=200)

    def __str__(self):
        return self.Name