from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text']);
		return redirect('/');

	items = Item.objects.all();
	return render(request, 'home.html', {'items': items});

def favicon(request):
	image_data = open("/Users/lewis/Development/TDD-Python/superlists/lists/favicon.ico", "rb").read();
	return HttpResponse(image_data);
