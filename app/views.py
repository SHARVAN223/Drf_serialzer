from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student as stu
from app.serializers import Stu_serializer 
from rest_framework.renderers import JSONRenderer
def student(req):
    data = stu.objects.all()
    serializer = Stu_serializer(data,many=True)
    print(serializer)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)
    return HttpResponse(json,content_type='application/json')
 