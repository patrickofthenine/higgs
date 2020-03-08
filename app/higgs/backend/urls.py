from django.urls import path
from backend.views import HiggsView

urlpatterns = [
	path('', HiggsView.as_view(), name='index')
]