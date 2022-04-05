from django.urls import path
from . import views

urlpatterns = [
    path('',views.supers_list),
    path('supers/<str:super_type_id>/',views.supers_list),
    path('<int:pk>/',views.supers_detail),
]