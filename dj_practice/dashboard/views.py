from django.shortcuts import render, redirect #, reverse
from django.views.generic import TemplateView
from django.conf import settings

from django.http import HttpResponseBadRequest, JsonResponse

from dashboard.thunder_coop_api.get_json import RawDataImporter, JsonDataGrabber, data_importer
from dashboard.thunder_coop_api.model_view import ViewFromModel
from dashboard.thunder_coop_api.serializers import NormalSerializer, Normal, BigRunSerializer, BigRun, TeamContestSerializer, TeamContest


class BaseView(TemplateView):
    def __init__(self, template_filename):
       super(BaseView, self).__init__()
       self.template_filename = template_filename


class Index(BaseView):
    def __init__(self):
        super().__init__(template_filename="index.html")

    def get(self, request, *args, **kwargs):
        view_from_model = ViewFromModel()
        phases = view_from_model.get_phases()

        return render(
            request,
            self.template_filename,
            {"current_json": phases}
        )

    

class DataIOView(BaseView):
    def __init__(self):
        super().__init__(template_filename="data_io.html")

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_filename,
            {}
        )

    def post(self, request, *args, **kwargs):
        if "action" in request.POST:
            action = request.POST["action"]
            if action == "get_data":
                data_importer()
                return JsonResponse({})
            if action == "export_data":
                return JsonResponse({})
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()

    