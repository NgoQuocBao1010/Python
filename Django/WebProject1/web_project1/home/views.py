from django.shortcuts import render
from WeddingDress.models import WeddingDress
from django.http import HttpResponse
# Create your views here.


def home(resquest):
	import random as rd

	dresses = WeddingDress.objects.all()
	ramdomPick = rd.choices(dresses, k=2)

	context = {
		'data': ramdomPick
	}

	return render(resquest, 'home/home.html', context)


def about(resquest):
	return render(resquest, 'home/about.html')