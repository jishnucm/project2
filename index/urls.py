from django.urls import path
from. import views

urlpatterns = [
    path('index3',views.home),
    path('index2',views.index2),
    path('index5',views.python)

]