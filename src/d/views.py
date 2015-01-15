from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage,\
    PageNotAnInteger
from d.models import DiguaUserApacheNotMacUntil2015

# def archive_d(request):
#     topics = DiguaUserApacheNotMacUntil2015.objects.all()
#     t = loader.get_template('index.html')
#     c = Context({'topics':topics})
#     return HttpResponse(t.render(c))



def archive_d(request):
    error = False
    each_page = 10
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            qset = (
                    Q(imei__icontains = q)
                    )
            record_list = DiguaUserApacheNotMacUntil2015.objects.filter(qset)
            paginator = Paginator(record_list,each_page)
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1
            try:
                contacts = paginator.page(page)
            except (EmptyPage, InvalidPage):
                contacts = paginator.page(paginator.num_pages)
            return render_to_response('all_record.html',{'record_list': contacts, 'query': q})#,'contacts':contacts})
    else:
        record_list = DiguaUserApacheNotMacUntil2015.objects.all()
        paginator = Paginator(record_list,each_page)
        
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
    return render_to_response('all_record.html',{'error':error,'record_list':contacts})#record_list,'contacts':contacts})