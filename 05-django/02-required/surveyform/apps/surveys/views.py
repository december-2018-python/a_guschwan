from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if "num" in request.session:
        request.session['num'] += 1
    else:
        request.session['num'] = 1
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
    return render(request, 'surveys/result.html')