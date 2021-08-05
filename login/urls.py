from django.urls import path
from . import views
urlpatterns=[
    path('login',views.login,name='login'),
    path('build',views.build,name='build'),
    path('make',views.make,name='make'),
]