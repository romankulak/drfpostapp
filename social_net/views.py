from django.shortcuts import render

def home(request):
    return render(request, "posts/post_list.html", {})