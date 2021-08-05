from django.urls import path
from . import views
urlpatterns=[
    path('register',views.register,name='register'),
    path('build',views.build,name='build'),
    path('make',views.make,name='make'),

]