from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from backend.models import Higgs

class HiggsView(View):
	def get(self, request):
		try:
			events = Higgs.objects.filter(class_label=1)[:10]
			return HttpResponse(events)
		except Exception as e:
			logging.warning(e)
