from django.urls import path
from .views import HistoryList,HistoryDetail

urlpatterns = [
    path('history/', HistoryList.as_view(), name='event_list'),
    path('history/<int:pk>/',HistoryDetail.as_view(), name='event_detail'),
]
