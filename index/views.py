import json
import logger

from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
from django.views import View
from django.views.generic import ListView

from index.models import MysiteSystem, WebsiteInfo

class IndexView(ListView):
    model_sys = MysiteSystem
    model_info = WebsiteInfo

    def get(self, request):
        sys_list = self.model_sys.objects.all()
        sys_list = serializers.serialize('json', sys_list)
        info = self.model_info.objects.all()
        info = serializers.serialize('json', info)

        return JsonResponse({'sys': json.loads(sys_list), 'info': json.loads(info)}, safe=False,
                            json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs):
        form = self.model_sys(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("succese/")
