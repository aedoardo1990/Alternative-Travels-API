from django.urls import path
from opinions import views


urlpatterns = [
    path('opinions/', views.OpinionList.as_view()),
    path('opinions/<int:pk>/', views.OpinionDetail.as_view())
]
