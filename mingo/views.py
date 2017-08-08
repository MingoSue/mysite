from django.shortcuts import render_to_response
from .form import Sighting, UserForm
from .models import Sighting as DB
from .models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

# 注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(username= username, password=password)
            return HttpResponseRedirect('/mingo/contact/')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username,password__exact=password)
            if user:
                # 比较成功，跳转contact
                response = HttpResponseRedirect('/mingo/contact/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/mingo/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

# 退出
def logout(req):
    response = HttpResponseRedirect('/mingo/login/')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response

def contact(request):
    return render_to_response('contact.html')

# 显示名单
def show_data(request):
    names = DB.objects.all()
    return render_to_response('show.html', locals())

# 报告数据
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