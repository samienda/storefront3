from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from rest_framework.views import APIView


class HellowView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2', timeout=50)
        data = response.json()

        return render(request, 'hello.html', {'name': "sami"})
