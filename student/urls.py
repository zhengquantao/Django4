from django.conf.urls import url
from student import views

urlpatterns = [

    url(r'course/(\d+)/', views.course),
    url(r'(\d+)/', views.classes),

]