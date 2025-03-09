from django.shortcuts import render
from testapp.form import tempform
from testapp.models import tempmodel
def tempview(request):
    form = tempform()
    name=''
    subbimited=False
    if request.method=='POST':
        form=tempform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            name=form.cleaned_data['name']
            subbimited=True
    else:
        print("validation error")

    return render(request,'testapp/res.html',{'name':name,'subbimited':subbimited,'form':form})
def baseview(request):
    return render(request,'testapp/base.html')
def dataview(request):
    data=tempmodel.objects.all()
    return render(request,'testapp/data.html',{'data':data})



