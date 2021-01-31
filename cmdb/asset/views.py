from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
# Create your views here.
from .models import Host
import os


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


def import_ajax(request):

    # 这里的file_obj拿到了文件的对象，这个对象包含了文件的名字，二进制内容
    # print(file_obj, type(file_obj))
    file_obj = request.FILES.get('file_obj')
    file_name = file_obj.name
    file_path = os.path.join(settings.BASE_DIR, 'files', file_name)
    from django.core.files.uploadedfile import InMemoryUploadedFile
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)


    return JsonResponse({'code' : 200, "msg": file_name})