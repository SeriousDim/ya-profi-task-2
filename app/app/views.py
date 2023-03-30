from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Group
from .serializers import GroupSerializer

@api_view(['POST'])
def group(request):
    name = request.data['name']
    desc = request.data['description'] if 'description' in request.data else ''
    obj = Group.objects.create(name=name, description=desc)
    return Response(obj.id)


@api_view(['GET'])
def groups(request):
    objs = Group.objects.all().values('id', 'name', 'description')
    return Response(objs)


@api_view(['GET'])
def group_id(request, id):
    obj = Group.objects.get(id=id)
    if not obj:
        return Response(status=status.HTTP_404_NOT_FOUND)

    obj = GroupSerializer(data=dict(obj))
    if obj.is_valid():
        return Response(obj.data)
    else:
        print(obj.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
