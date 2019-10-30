from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, "untitled.html", {})

def home_page_old(request):
	return HttpResponse('<html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body><h1>sgsdghfhyr</h1><p>gsgsgsg</p><a href="">yujdrtuder</a></body></html>')