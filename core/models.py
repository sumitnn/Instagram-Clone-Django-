from django.db import models
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from .managers import MyUserManager

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(verbose_name='DOB',blank=True,null=True)
    username=models.CharField(verbose_name='Username',max_length=30,unique=True)
    fullname=models.CharField(verbose_name='FullName',max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','fullname']

    def __str__(self):
        return f"email:{self.email},username={self.username},is_active={self.is_active} "

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin