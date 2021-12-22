# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models
# from django.utils import timezone

# # Create your models here.

# class UserManager(BaseUserManager):

# 	def _create_user(self, email, password, is_staff, is_superuser, **extra_fileds):
# 		if not email:
# 			raise ValueError('Users must have an email address')
# 		now = timezone.now()
# 		email = self.normalize_email(email)
# 		user = self.model(
# 			email=email,
# 			is_staff=is_staff,
# 			is_active=True,
# 			is_superuser=is_superuser,
# 			last_login=now,
# 			date_joined=now,
# 			**extra_fields)

# 		user.set_password(password)
# 		user.save(using=self._db)
		
# 		return user

# 	def create_user(self, email, password, **extra_fields):
# 		return self._create_user(email, password, False, False **extra_fields)

# 	def create_superuser(self, email, password, **extra_fields):
# 		user=self._create_user(email, password, True, True, **extra_fields)
# 		user.save(using=self.db)
# 		return user

# class User(AbstractBaseUser, PermissionsMixin):
# 	email = models.EmailField(max_length=254, unique=True)
# 	name = models.CharField(max_length=254, unique=True)
# 	is_staff = models.BooleanField(default=False)
# 	is_superuser = models.BooleanField(default=False)
# 	last_login = models.DateTimeField(null=True, blank=True)
# 	date_joined = models.DateTimeField(auto_now_add=True)

# 	USERNAME_FIELD = 'email'
# 	EMAIL_FIELD = 'email'
# 	REQUIRED_FIELDS = []

# 	objects = UserManager()

# 	def get_absolute_url(self):
# 		return"/users/%i/" % (self.pk)





# class NewUser():

# 	email = models.EmailField(gettext_lazy('email address'), (unique=True))
# 	user_name = models.CharField(max_length=150)
# 	first_name = models.CharField(max_length=150), (unique=True)
# 	start_date = models.DateTimeField(default=timezone.now)
# 	about = models.Textfield(gettext_lazy(
# 		'about'), max_lenth=500, blank=True)
# 	is_staff = models.BooleanField(default=False)
# 	is_active = models.BooleanField(default=False)

# class Employee():
# 	email = models.EmailField(gettext_lazy('email address'), (unique=True))
# 	user_name = models.CharField(max_length=150)
# 	first_name = models.CharField(max_length=150), (unique=True)
# 	start_date = models.DateTimeField(default=timezone.now)
# 	about = models.Textfield(gettext_lazy(
# 		'about'), max_lenth=500, blank=True)
# 	is_staff = models.BooleanField(default=False)
# 	is_active = models.BooleanField(default=False)

# class Employer():
# 	email = models.EmailField(gettext_lazy('email address'), (unique=True))
# 	user_name = models.CharField(max_length=150)
# 	first_name = models.CharField(max_length=150), (unique=True)
# 	start_date = models.DateTimeField(default=timezone.now)
# 	about = models.Textfield(gettext_lazy(
# 		'about'), max_lenth=500, blank=True)
# 	is_staff = models.BooleanField(default=False)
# 	is_active = models.BooleanField(default=False)