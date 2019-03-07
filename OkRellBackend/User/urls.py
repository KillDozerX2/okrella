"""
OkRell urls for the User app.
Include specific views here.
"""
from django.urls import path, include
from User.views import UserListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'allUsers', UserListView)

urlpatterns = [
	path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]