from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from buginfo.models import BugInfo
from buginfo.serializers import BugInfoSerializer
from rest_framework.views import APIView


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class BugInfoView(APIView):
    def  post(self,request):
        data = JSONParser().parse(request)
        serializer = BugInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        return JSONResponse(serializer.errors, status=400)
