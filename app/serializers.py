from rest_framework import serializers

class Stu_serializer(serializers.Serializer):
    Name = serializers.CharField(max_length=50)
    Age = serializers.IntegerField()
    City = serializers.CharField(max_length=50)
    Contact = serializers.CharField(max_length=15)



    