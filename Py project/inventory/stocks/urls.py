from django.urls import path

from .views import *

urlpatterns = [
    path('location/create', LocationCreate.as_view(), name='index'),
    path('company/create', CompanyCreate.as_view(), name='company'),
    path('company/<int:pk>', CompanyDetail.as_view(), name='get_company'),
    path('company/list', CompanyListView.as_view(), name='get_company'),

]