from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def blog_list(request):
    context={
        'title':'Some title',
        'description':'Some description'
    }
    print(settings.BASE_DIR)
    return JsonResponse(context)

def home(request):
    print(settings.BASE_DIR)
    return render(request,'blog/index.html',{})
