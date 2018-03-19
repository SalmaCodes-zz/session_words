from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


# Create your views here.

# '/' OR '/session_words'
def index(request):
    return render(request,'words/index.html')


# '/session_words/add'
def add(request):
    if 'words' not in request.session:
        request.session['words'] = []

    if 'size' not in request.POST:
        size = 'small'
    else:
        size = request.POST['size']
    
    time = strftime("%I:%M:%S %p, %B %d %Y", gmtime())

    wordslist = request.session['words']
    wordslist.append({
        'word': request.POST['word'],
        'color': request.POST['color'],
        'size': size,
        'time': time
    })
    request.session['words'] = wordslist
    return redirect('/session_words')


# '/session_words/clear'
def clear(request):
    request.session['words'] = []
    return redirect('/session_words')