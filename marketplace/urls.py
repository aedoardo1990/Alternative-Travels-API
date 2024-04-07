from django.urls import path
from marketplace import views

urlpatterns = [
    path('marketplace/', views.MarketplaceList.as_view()),
    path('marketplace/<int:pk>', views.MarketplaceDetail.as_view()),
]
