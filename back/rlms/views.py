import json

from django.http import HttpResponse
from rest_framework.decorators import api_view

from rlms.models import Listing


@api_view(['GET', 'POST', 'DELETE'])
def listings(request):
    if request.method == 'GET':
        data = Listing.objects.values()
        values = [x for x in data]
        return HttpResponse(json.dumps(values))
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        id = request.query_params['id']
        instance = Listing.objects.get(id=id)
        result = instance.delete()
        print(result, instance)
        return HttpResponse(f'{instance.Address} deleted')
