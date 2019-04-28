from django.views.generic import View
from django.shortcuts import render, redirect

class BaseView(View):
    def get(self, request):
        response_params = {}
        return render(request, 'stream.html', response_params)