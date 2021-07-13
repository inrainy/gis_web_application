from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'model_instance':model_instance})

    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'GET METHOD!'})
    #대소문자 틀리면 안됨 HttpResponse
    #http에서 alt + enter누르면 뭐가 뜸