# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Umedul 70")
    return render(request , 'index.html')


def analyse(request):
    text = request.POST.get('text','default')
    opt = request.POST.get('opt','off')
    anatext =""
    if opt == 'removepunc':
        punchuations = '''*&^%$#@!><?:;'"'''
        for char in text:
            if char not in punchuations:
                anatext = anatext + char
        params = {'purpose':'Remove Punchuations', 'anatext': anatext }
    elif opt == 'upper':
        for char in text:
            anatext = anatext + char.upper()
            params = {'purpose':'Uppercase', 'anatext': anatext }
    elif opt == 'removenewline':
        for char in text:
            if char != "\n" and char != '\r':
                anatext=anatext + char
            params = {'purpose':'New Line Remove', 'anatext': anatext }
    elif opt == 'removeextraspace':
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index + 1] == " "):
                anatext = anatext + text[index]
            params = {'purpose':'Remove Extra Space', 'anatext': anatext }

    elif opt == 'count':
        count = 0
        for index, char in enumerate(text):
            count += 1
        a = f"number of character in your text is : {count}"
        params = {'purpose':'Character Count', 'anatext': a }
            
    else:
        return HttpResponse("Error")
    return render(request, 'analyse.html', params)
    
    
