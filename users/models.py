from django.db import models

# Create your models here.

class NewUser():

	email = models.EmailField(gettext_lazy('email address'), (unique=True))
	user_name = models.CharField(max_length=150)
	first_name = models.CharField(max_length=150), (unique=True)
	start_date = models.DateTimeField(default=timezone.now)
	about = models.Textfield(gettext_lazy(
		'about'), max_lenth=500, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

class Employee():
	email = models.EmailField(gettext_lazy('email address'), (unique=True))
	user_name = models.CharField(max_length=150)
	first_name = models.CharField(max_length=150), (unique=True)
	start_date = models.DateTimeField(default=timezone.now)
	about = models.Textfield(gettext_lazy(
		'about'), max_lenth=500, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

class Employer():
	email = models.EmailField(gettext_lazy('email address'), (unique=True))
	user_name = models.CharField(max_length=150)
	first_name = models.CharField(max_length=150), (unique=True)
	start_date = models.DateTimeField(default=timezone.now)
	about = models.Textfield(gettext_lazy(
		'about'), max_lenth=500, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)