from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import Host


def index(request):
    return render(request, 'asset/list.html')


def list_ajax(request):
    # hosts = Host.objects.all()
    # for host in hosts:
    #     print(dir(host))
        
    result= [model_to_dict(host) for host in Host.objects.all()]
    return JsonResponse({'code' : 200, 'result' : result})


def get_ajax(request):
    _id = request.GET.get('id', 0)
    try:
        host = Host.objects.get(pk=_id)
        print(host)
        return JsonResponse({'code' : 200, 'result' : model_to_dict(host)})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code': 400, 'result': {}})

def delete_ajax(request):
    _id = request.GET.get('id',0)
    try:
        Host.objects.get(pk=_id).delete()
    except ObjectDoesNotExist as e:
        pass
    return JsonResponse({'code' : 200})
