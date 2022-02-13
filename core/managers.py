from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, fullname,username, password=None):
       
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError('Users must have an Username')
        

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            username=username,

        )
        user.set_password(password)  
        user.is_active=True
        user.is_verify= False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname,username, password=None):
        
        user = self.create_user(
            email=self.normalize_email(email),
            fullname=fullname,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active=True
        user.is_verify= True
        user.save(using=self._db)
        return user