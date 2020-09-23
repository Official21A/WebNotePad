from django.urls import path, include

app_name = 'users'

urlpatterns = [
	# add the first page show to users
	path('', include('django.contrib.auth.urls')),
]