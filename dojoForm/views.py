from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'POST':
        print("a POST is being made to this route")
        context = {
            "name" : request.POST["name"],
            "email" : request.POST["email"],
        }
        return render(request, "result.html", context)
    else:
        return redirect('')