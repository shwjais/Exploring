from django.conf.urls import url
from level_five_app import views

app_name='level_five_app'

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
]