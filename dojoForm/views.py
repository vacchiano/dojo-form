from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'POST':
        print("a POST is being made to this route")
        return HttpResponse("POST recieved")