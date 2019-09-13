from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.utils import timezone
from .models import Group,Tool
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    today_groups = Group.objects.order_by('-work_date')

    context = {'today_groups': today_groups}
    return render(request,'UI/index.html', context)


def detail(request,group_id):

    group = get_object_or_404(Group,pk=group_id)
    return render(request,'UI/detail.html',{'group':group})

def revise(request,group_id):
    group = get_object_or_404(Group,pk=group_id)
    try:
        selected_tool=group.tool_set.get(pk=request.POST['tool'])
    except (KeyError,Tool.DoesNotExist):
        return render(request,'UI/detail.html',{'group':group,'error_message':"你没有修改！"})
    else:
        selected_tool.num_tools +=10
        selected_tool.save()

        return HttpResponseRedirect(reverse('UI:results',args=(group.id,)))

def results(request , group_id):
    group = get_object_or_404(Group,pk=group_id)
    return render(request,'UI/results.html',{'group':group})