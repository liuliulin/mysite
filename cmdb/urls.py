from django.conf.urls import url
from cmdb import views

urlpatterns = [
    url(r'home/', views.home, {'user': 'user_ojb'}),
]