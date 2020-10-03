from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Router
from .forms import RouterForm


def router_list(request):
    routers = Router.objects.filter(is_deleted=False)
    return render(request, 'routers/router_list.html', {'routers': routers})


def save_router_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            routers = Router.objects.filter(is_deleted=False)
            data['html_router_list'] = render_to_string('routers/includes/partial_router_list.html', {
                'routers': routers
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def router_create(request):
    if request.method == 'POST':
        form = RouterForm(request.POST)
    else:
        form = RouterForm()
    return save_router_form(request, form, 'routers/includes/partial_router_create.html')


def router_update(request, pk):
    router = get_object_or_404(Router, pk=pk)
    if request.method == 'POST':
        form = RouterForm(request.POST, instance=router)
    else:
        form = RouterForm(instance=router)
    return save_router_form(request, form, 'routers/includes/partial_router_update.html')


def router_delete(request, pk):
    router = get_object_or_404(Router, pk=pk)
    data = dict()
    if request.method == 'POST':
        router.is_deleted = True
        print(router.is_deleted)
        router.save()
        data['form_is_valid'] = True
        routers = Router.objects.filter(is_deleted=False)
        data['html_router_list'] = render_to_string('routers/includes/partial_router_list.html', {
            'routers': routers
        })
    else:
        context = {'router': router}
        data['html_form'] = render_to_string('routers/includes/partial_router_delete.html', context, request=request)
    return JsonResponse(data)
