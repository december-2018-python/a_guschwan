from django.shortcuts import render, redirect
from time import strftime
# Create your views here.
def swords(request):
    return render(request, 'swords/session_words.html')

def wordit(request):
    try:
      if words not in request.session:
            words = []
            request.session['words'] = words
    except:
            words  = []
            request.session['words'] = words

    word = request.POST['word'] + " added on " + strftime(" %I:%M %p %b %d, %Y")
    color = request.POST['color']
    bigfont = request.POST['bigfont']
    dict = {"worda":word, "colora":color, "bigfonta": bigfont}  
    temp_list = request.session['words']
    temp_list.append(dict)
    request.session['words'] = temp_list
    print(temp_list)
    return redirect("/session_words")