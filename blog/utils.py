from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Post, Tag
from django.views.generic import View

class ObjectDetailMixin:
    model = None
    template = None
    def get(self,request,slug):

        n = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): n, 'admin_obj':n, 'detail_view':True})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self,request):
        form = self.model_form()
        return render(request,self.template, context={'form': form})

    def post(self, request):

        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template, context={'form': bound_form})
class ObjectUpdateMixit:
    model = None
    model_form = None
    template = None
    def get(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,self.template, context={'form':bound_form,self.model.__name__.lower():obj})
    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template, context={'form':bound_form,self.model.__name__.lower():obj})
class ObjDeleteMixin:
    model = None
    template = None
    redirect_url = None
    def get(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})
    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
