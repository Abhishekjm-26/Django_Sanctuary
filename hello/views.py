from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from hello.models import sanctuary
from django.views import generic
# Create your views here.

def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'contact.html')

def current_datetime(request):
    now = datetime.datetime.now()
    l=["invertibrates","fish","reptiles","birds","mammals"]
    return render(request,'dt.html', {'now': now, 'daylist' : l})


def hour_offset(request, plus_or_minus, offset): 
    offset = int(offset)
    if offset == 1:
        hours = 'hour' 
    else:
        hours = 'hours'
    if plus_or_minus == 'plus':
        dt = datetime.datetime.now() + datetime.timedelta(hours=offset) 
        output = 'In %s %s, it will be %s.' % (offset, hours, dt)
    else:
        dt = datetime.datetime.now() - datetime.timedelta(hours=offset) 
        output = '%s %s ago, it was %s.' % (offset, hours, dt)
        output = '<html><body>%s</body></html>' % output 
    return HttpResponse(output)

def add_san(request): 
    submitted = False
    if request.method == 'POST': 
        form = OrderForm(request.POST) 
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add/?submitted=True')
    else:
        form = OrderForm()
        if 'submitted' in request.GET: 
            submitted = True
    aoc = request.session.get('aoc', 0) 
    request.session['aoc'] = aoc + 1
    return render(request, 'add_order.html', {'nv':request.session['aoc'],'form': form, 'submitted': submitted})

class sanctListView(generic.ListView): 
    model = sanctuary
    template_name = 'sanctuary_manage.html' 
    paginate_by = 10


