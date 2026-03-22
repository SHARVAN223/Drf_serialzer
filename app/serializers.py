from rest_framework import serializers
from app.models import Student

class Stu_serializer(serializers.Serializer):
    Name = serializers.CharField(max_length=50)
    Age = serializers.IntegerField()
    City = serializers.CharField(max_length=50)
    Contact = serializers.CharField(max_length=15)\
    


    def create(self,validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance,validated_data):
        instance.Name = validated_data.get('name',instance.Name)
        instance.Age = validated_data.get('age',instance.Age)
        instance.Contact = validated_data.get('contact',instance.Contact)
        instance.City = validated_data.get('city',instance.City)
        instance.save()
        return instance




    


    