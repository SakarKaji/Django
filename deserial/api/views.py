from django.shortcuts import render, HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.
@csrf_exempt #like django expecting forms to have csrf_token , for third party applicaiton we use exempt
def student_create(request):
    if request.method == 'POST': #from myapp.py we are sending post request
        json_data = request.body
        stream = io.BytesIO(json_data) #convert json data to stream
        pythondata = JSONParser().parse(stream) #converts stream to pythondata
        serializer = StudentSerializer(data=pythondata) #start of deserialization
        if serializer.is_valid(): #check if complex data is validated , check if it is capable to save it in our database
            serializer.save()
            responseMessage = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(responseMessage)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data, content_type='application/json')
        
