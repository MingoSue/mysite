from django.shortcuts import render
from django.shortcuts import render_to_response
from .form import Sighting
from .models import Sighting as DB
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.

def contact(request):
    return render_to_response('contact.html')

def form_page(request):
    if request.method == 'POST':  # 如果表单提交
        form = Sighting(request.POST)  # 绑定数据到表单
        if form.is_valid():  # 验证所有规则
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            data = form.cleaned_data['data']
            time = form.cleaned_data['time']
            location = form.cleaned_data['location']
            fin_type = form.cleaned_data['fin_type']
            whale_type = form.cleaned_data['whale_type']
            blow_type = form.cleaned_data['blow_type']
            wave_type = form.cleaned_data['wave_type']
            DB.objects.create(name=name, email=email, data=data, time=time,
                              location=location, fin_type=fin_type,
                              whale_type=whale_type, blow_type=blow_type,
                              wave_type=wave_type)

            return render_to_response('base.html')  # Post提交后跳转
    else:
        form = Sighting()  # 空表单

    return render_to_response('form.html', {
        'title': 'Report a Sighting',
        'form': form,
        'links': 'Home',
    }, context_instance=RequestContext(request))