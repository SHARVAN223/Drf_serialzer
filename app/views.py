from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Student as stu
from app.serializers import Stu_serializer 
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student(req):
    if req.method == 'POST':
        data = req.body
        strame = io.BytesIO(data)
        p_data= JSONParser().parse(strame)
        serializer=Stu_serializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            print({'msg': 'object created'})
            return HttpResponse({'msg':'object created'},content_type='application/json')
           
        else:
            data=JSONRenderer().render(serializer.errors)
            return HttpResponse(data,content_type='application/json')


    data = stu.objects.all()
    serializer = Stu_serializer(data,many=True)
    print(serializer)
    print(serializer.data)
    # data = stu.objects.get(id=1)
    # serializer = Stu_serializer(data)
    # print(serializer)
    # print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)
    return HttpResponse(json,content_type='application/json')
 