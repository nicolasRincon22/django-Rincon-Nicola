from django.shortcuts import render
import datetime

# Create your views here.
def es_if(request) :
    context = {
        'var1' : 100,
        'var2' : 100,
        'var3' : 300
    }
    return render(request, "es_if.html", context)
def if_else_elif(request):
    context = {
        'var1' : 100,
        'var2' : 100.0,
        'var3' : 100.50,
    }
    return render(request, "if_else_elif.html", context)
def es_for(request):
    context = {
        'List1': [1, datetime.date(2019,7,16), 'Do not give up!'],
        'List2': [1, datetime.date(2019,7,16), 'Do not give up!']
    }
    return render(request, "es_for.html", context)
def  index(request):
    return render(request,"index.html")