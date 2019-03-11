from django.shortcuts import render
# from django.contrib.auth.models import User
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from User.serializers import UserSerializer
# Create your views here.

class UserListView(viewsets.ModelViewSet):
	# """
	# API endpoint that allows users to be viewed or edited.
	# """
	# queryset = User.objects.all().order_by('-date_joined')
	# serializer_class = UserSerializer
	pass

		
def confirmUserView(request):
	if request.method == "POST":
		UserModel = get_user_model()
		activate_user_message = UserModel.objects.get(email=request.POST["UserEmail"]).activate_user(submitted_token=request.POST["Code"])
		print(activate_user_message)
	return render(request, template_name='userconfirmation.html')