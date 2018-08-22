from django.shortcuts import render

# Create your views here.


def gf_index(request):
    data = {}
    return render(request, 'portal/index.html', data)