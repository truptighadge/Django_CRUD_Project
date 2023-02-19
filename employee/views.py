from django.shortcuts import render,redirect
# Create your views here.
from .models import Info
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import messages

from .forms import InfoForm,UpdateForm,DelForm

from  django.urls import reverse

def home (request):
	return render(request,"home.html")


def insert (request,uid=1):   # Create   
	if request.method=='POST':
		inform=InfoForm(request.POST)
		if inform.is_valid():
			inform.save()
			messages.info(request,"Information Stored Successfully")
			return redirect(reverse("employee:display"))
		else:
			messages.info(request,"Invalid Information")
			return HttpResponseRedirect(reverse("employee:insert"))
	else:
	    inform=InfoForm()
	    return render(request,"insert.html",{'inform':inform})


def display(request):        #Read
	data=Info.objects.all()
	#return HttpResponse("<br>".join([e.name for e in data]))
	context={"data":data}
	return render(request,'display.html',context)




	  
def update(request):
	#return HttpResponse("<h1>Update Page</h1>")
	if request.method == 'POST':
		upform = UpdateForm(request.POST)
		if upform.is_valid():
			uid=request.POST.get('uid','')
			new_name=request.POST.get('name','')

			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.update(name=new_name)
				messages.info(request, "Name updated successfully")
				return redirect(reverse("employee:display"))
			else:
				messages.info(request, "Invalid uid, not found in database")
				return redirect(reverse("employee:update"))

		else:
			messages.info(request, "Invalid data")
			return redirect(reverse("employee:update"))
	else:
		upform=UpdateForm()
		return render(request, "update.html",{'upform':upform})					


def delete(request):
	#return HttpResponse("<h1>Delete Page</h1>")
	if request.method == 'POST':
		delform = DelForm(request.POST)
		if delform.is_valid():
			uid=request.POST.get('uid','')
			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.delete()
				messages.warning(request, "Record Deleted successfully")
				return redirect(reverse("employee:display"))
			else:
				messages.warning(request, "Invalid uid, not found in database")
				return redirect(reverse("employee:delete"))

		else:
			messages.warning(request, "Invalid data")
			return redirect(reverse("employee:delete"))
	else:
		delform=DelForm()
		return render(request, "delete.html",{'delform':delform})					


 	