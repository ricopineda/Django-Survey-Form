# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'user_app/index.html')

def process(request):
	if request.method == "POST":
		request.session['name'] = request.POST["name"]
		request.session['location'] = request.POST["location"]
		request.session['language'] = request.POST["language"]
		request.session['comments'] = request.POST["comments"]
		print request.POST

		print "hola"


		return redirect('/results')
	else:
		return redirect("/")


def results(request):

	return render(request,'user_app/results.html')