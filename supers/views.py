from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from super_types.models import Type
from django.shortcuts import get_object_or_404





@api_view(['GET','POST']) #HTTP request parameters return custom_response + Get all Heroes
def supers_list(request):
    if request.method == 'GET':
        custom_response_dictionary = {}
        type_param = request.query_params.get('type')
        supers = Super.objects.all()

        if type_param:
            supers = supers.filter(super_type__type = type_param)
            serializer = SuperSerializer(supers,many = True)
            return Response(serializer.data)
        else:
            super_types = Type.objects.all()
            for type in super_types:
                supers = Super.objects.filter(super_type_id = type.id)
                serializer = SuperSerializer(supers, many = True)
                custom_response_dictionary[type.type] = serializer.data

            return Response(custom_response_dictionary)

  
  
@api_view(['GET','PUT','DELETE'])
def supers_detail(request,pk):
  super = get_object_or_404(Super,pk=pk)
  
  if request.method == 'GET':
    serializer = SuperSerializer(super)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  elif request.method == 'PUT':
    serializer = SuperSerializer(super, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  elif request.method == 'DELETE':
    super.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
