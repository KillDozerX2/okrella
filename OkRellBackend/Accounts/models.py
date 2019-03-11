import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class SiteUserManager(BaseUserManager):
	
	def create_user(self, email, first_name,
		last_name, date_of_birth, password=None, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("All users must have an email")
		if not password:
			raise ValueError("All users must have a password")
		user_obj = self.model(
			email = self.normalize_email(email)
		)
		user_obj.set_password(password)
		user_obj.first_name = first_name
		user_obj.last_name = last_name
		user_obj.date_of_birth = date_of_birth
		user_obj.date_joined = datetime.datetime.now()
		user_obj.active = False
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		## Send confirmation email code here.
		tokenGen = PasswordResetTokenGenerator()
		user_obj.reset_token = tokenGen.make_token(user=user_obj)
		send_mail(
		    'Ok Rella account confirmation',
		    'Welcome to Ok Rella \n here is you confirmation code :- ' + user_obj.reset_token,
		    'hp1himanshupant27598@gmail.com',
		    [user_obj.email],
		    fail_silently=False,
		)
		# The user won't be saved if email failed
		user_obj.save(using=self._db)
		return user_obj
		
	def create_staffuser(self, email, first_name, last_name, date_of_birth, password=None):
		new_staff_member = self.create_user(email, 
			first_name, last_name, date_of_birth, password=None, is_staff=True)
		return new_staff_member
	def create_superuser(self, email, first_name, last_name, date_of_birth, password=None):
		new_super_user = self.create_user(email, 
			first_name, last_name, date_of_birth, password, is_staff=True, is_admin=True)
		return new_super_user


class SiteUser(AbstractBaseUser, PermissionsMixin):
	first_name 		= models.CharField(max_length=25, verbose_name="First Name", default="John")
	last_name		= models.CharField(max_length=25, verbose_name="Last Name", default="Doe")
	date_of_birth 	= models.CharField(max_length=10, verbose_name="Date of birth")
	date_joined		= models.DateTimeField(auto_now_add=True, verbose_name="Date User joined")
	email 			= models.EmailField(max_length=255, unique=True,
		default="johnDoe@okrella.com", verbose_name="Email of user")
	reset_token 		= models.CharField(max_length=255, verbose_name="Reset Token")
	 #can login, default set to false and will need an email confirmation to become active
	active			= models.BooleanField(default=False, verbose_name="User is active")
	staff 			= models.BooleanField(default=False, verbose_name="User is staff") #is staff member but not super user
	admin			= models.BooleanField(default=False, verbose_name="User is admin") #is superuser of the site.


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [
		'first_name', 'last_name', 'date_of_birth'
	]
	objects = SiteUserManager()

	def __str__(self):
		return self.first_name + " " + self.last_name + " - " + self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.first_name

	@property
	def is_active(self):
		return self.active
	
	@property
	def is_staff(self):
		return self.staff

	@property
	def is_superuser(self):
		return self.admin

	@is_staff.setter
	def is_staff(self, value):
		self.staff = value

	def has_perm(self, perm, obj=None):
		return self.staff

	def has_module_perms(self, app_label):
		return self.admin

	def activate_user(self, submitted_token):
		if self.reset_token == submitted_token:
			self.active = True
			self.save()
			return "User activated"
		else:
			return "Token is invalid. User not activated"
		
	def reset_password(self, new_password=None, submitted_token=None):
		if not submitted_token:
			tokenGen = PasswordResetTokenGenerator()
			self.reset_token = tokenGen.make_token(user=user_obj)
			self.active = False
			self.save()
			send_mail(
			    'Ok Rella account password reset',
			    'Here is you reset code :- ' + user_obj.reset_token,
			    'hp1himanshupant27598@gmail.com',
			    [user_obj.email],
			    fail_silently=False,
			)
			return "Rest password email has been sent"
		else:
			if not new_password:
				raise ValueError("Invalid Password")
			else:
				self.set_password(new_password)
				return "Password has been reset"