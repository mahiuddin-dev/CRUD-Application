from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .forms import LeadsForm
from .models import Leads
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    leads = Leads.objects.all().order_by('-id')
    
    paginator = Paginator(leads, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = json.dumps(list(Leads.objects.values().order_by('-id')))

    context = {'page_obj': page_obj,'data':data}

    return render(request, 'index.html', context)

def search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        leads = Leads.objects.filter(name__icontains=search_text)
        paginator = Paginator(leads, 10) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'index.html', {'page_obj': page_obj})
    else:
        return render(request, 'index.html')


def save_leads_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            
            data['form_is_valid'] = True
            
            leads = Leads.objects.all().order_by('-id')
            paginator = Paginator(leads, 10) 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            data['html_book_list'] = render_to_string('leads_list.html', {
                'page_obj': page_obj
            })
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def merge_dictionaries(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the b ones
    return c


def save_leads_update(request, form, template_name,contextvalue):
    data = dict()
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            
            data['form_is_valid'] = True
            
            leads = Leads.objects.all().order_by('-id')
            paginator = Paginator(leads, 10) 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            data['html_book_list'] = render_to_string('leads_list.html', {
                'page_obj': page_obj
            })
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    merged_context = merge_dictionaries(context, contextvalue)

    data['html_form'] = render_to_string(template_name, merged_context, request=request)
    return JsonResponse(data)


def leads_create(request):
    if request.method == 'POST':
        form = LeadsForm(request.POST)
    else:
        form = LeadsForm()
    return save_leads_form(request, form, 'leads_create.html')

def leads_update(request, pk):
    book = get_object_or_404(Leads, pk=pk)

    if request.method == 'POST':
        form = LeadsForm(request.POST, instance=book)
    else:
        form = LeadsForm(instance=book)
    
    contextvalue = {'name':book.name,'phone':book.phone,'email':book.email,'designation':book.designation}

    return save_leads_update(request, form, 'leads_update.html',contextvalue)


def leads_delete(request, pk):
    book = get_object_or_404(Leads, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        
        books = Leads.objects.all().order_by('-id')
        paginator = Paginator(books, 60) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
            
        
        data['html_book_list'] = render_to_string('leads_list.html', {
            'page_obj': page_obj
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('leads_delete.html', context, request=request)
    return JsonResponse(data)