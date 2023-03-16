from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Filim
from . forms import FilimForm

# Create your views here.
def index(request):
    filim=Filim.objects.all
    context={
        'filim_list':filim

    }
    return render(request,'index.html',context)
def detail(request,filim_id):
    filim=Filim.objects.get(id=filim_id)
    return render(request,"detail.html",{'filim':filim})

def add_filim (request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        filim=Filim(name=name,desc=desc,year=year,img=img)
        filim.save()
    return render(request,'add.html')

def update(request,id):
    filim=Filim.objects.get(id=id)
    form=FilimForm(request.POST or None, request.FILES,instance=filim)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'filim':filim})
def delete(request,id):
    if request.method=='POST':
        filim=Filim.objects.get(id=id)
        filim.delete()
        return redirect('/')
    return render(request,'delete.html')