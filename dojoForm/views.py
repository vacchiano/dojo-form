from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
        return redirect("/result")
    else:
        return render(request, "index.html")

def result(request):
    # if request.method == 'POST':
    #     print("a POST is being made to this route")
    #     request.session['name'] = request.POST["name"]
    #     request.session['email'] = request.POST["email"]
    return render(request, "result.html")
    # else:
    #     return redirect('')