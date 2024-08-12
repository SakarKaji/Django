from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
# from django.http import JsonResponse

# Model Object - Single Student Data 
# Create your views here.
def student_detail(request, pk):
    stu = Student.objects.get(id=pk) #first make model object (which is considered as python data object)
    # print(stu)
    serializers = StudentSerializer(stu) #convert complex data type to python object
    # print(serializers)
    # print(serializers.data)
    json_data = JSONRenderer().render(serializers.data)  #convert python to json
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json') #we pass json to client
    # return JsonResponse(serializer.data) same as 14 and 16 line this shortens the code

#Query Set -> ALl Student Data
def student_list(request):
    stu = Student.objects.all() #first make model object (which is considered as python data object)
    # print(stu)
    serializers = StudentSerializer(stu, many=True) #convert complex data type to python object
    # print(serializers)
    # print(serializers.data)
    json_data = JSONRenderer().render(serializers.data)  #convert python to json
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json') #we pass json to client