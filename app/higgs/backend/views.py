from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db import models
# Create your views here.

def index(View):
	try:
		return HttpResponse('res')
	except Exception as e:
		logging.warning(e)
