from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

from typing import Union

import csv

from . import models
from . import forms 

class SuccessView(View):
    template = 'application/success.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request = request, template_name = self.template)

class IndexView(View):
    redirect_to = 'success'
    form_template = 'application/index.html'
    model = models.Application
    form = forms.ApplicationForm

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form()

        return render(
            request = request,
            template_name = self.form_template,
            context = {'form': form}
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> Union[HttpResponse, HttpResponseRedirect]:
        form = self.form(data = request.POST)

        is_valid = form.is_valid()
        if is_valid:
            form.save()
            return HttpResponseRedirect(
                redirect_to = self.redirect_to
            )

        return render(
            request = request,
            status = 400,
            template_name = self.form_template,
            context = {'form': form}
        )

class UploadView(View):
    filename = 'applications.csv'
    model = models.Application
    header = ('name', 'surname', 'phone', 'applied_at')

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = f'attachment; filename="{self.filename}"'

        writer = csv.writer(response)
        writer.writerow(self.header)

        data = self.model.objects.all()
        for row in data:
            writer.writerow(row.row())

        return response

