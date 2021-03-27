from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        url = requests.get(f"https://www.instagram.com/{username}/?__a=1", headers={'User-agent':'MyBot'}).json()
        user_info = url[f"{'graphql'}"][f"{'user'}"]
        return render(request,'index.html', {'user_info': user_info})
    else:
        return render(request,'index.html')