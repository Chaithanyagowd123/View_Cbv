from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View,TemplateView
from app.forms import *


#returning string as response ny using fbv
def fbv_string(request):
    return HttpResponse('<h1>this is the string of fbv </h1>')


#returning string as respomse by using cbv

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1> these is the string of cbv </h1>')
    


# rendering html by functional based view
def fbv_html(request):
    return render(request,'fbv_html.html')


#rendering html by class based view
class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    

# insert form by fbv
def insert_form(request):
    SFO=SchoolForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insertSchool_by_fbv_is_done')
        
    return render(request,'insert_form.html',d)



# inserting data by uing class base view
class insert_form_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_form_cbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if  SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert data by cbv is done')
        
    
class cbv_Template(TemplateView):
    template_name='cbv_Template.html'


    








