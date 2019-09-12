from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.utils import timezone
from .models import Group
from django.shortcuts import render


def index(request):
    today_groups = Group.objects.order_by('-work_date')

    context = {'today_groups': today_groups}
    return render(request,'UI/index.html', context)
