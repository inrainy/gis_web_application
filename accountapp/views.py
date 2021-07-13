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

        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'data_list':data_list})

    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list':data_list})
    #대소문자 틀리면 안됨 HttpResponse
    #http에서 alt + enter누르면 뭐가 뜸