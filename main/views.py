from django.shortcuts import render


def index(request):
    return render(requset, "main/index.html")
