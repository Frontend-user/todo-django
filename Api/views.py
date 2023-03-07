from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import SpisokForm, TaskForm
from .models import SpisokModel, TaskModel


def index(request):
    return render(request, 'Api/index.html')


def spisok(request):
    return render(request, 'Api/spisok.html')


def spisok_add(request):
    if request.method == 'POST':
        form = SpisokForm(request.POST)
        if form.is_valid():
            spisok_name = form.cleaned_data['spisok_name']
            SpisokModel.objects.create(spisok_name=spisok_name)
            all_spisok_names = SpisokModel.objects.filter()
            return render(request, 'Api/spisok.html',
                          {'spisok_name': [s.dict() for s in all_spisok_names]})
        return render(request, 'Api/spisok.html')
    elif request.method == 'GET':
        # all_lists = List_model.objects.filter()
        # return render(request, 'Api/spisok.html',
        #               {'name': [l.dict() for l in all_lists]})
        return render(request, 'Api/false.html')


def false_index(request):
    return redirect('false_index')


def tasks(request, spisok_id):
    # spisok = TaskModel.objects.get(spisok_id)
    # all_tasks = spisok.
    task = TaskModel.objects.get(id=spisok_id).task_name

    return render(request, 'Api/tasks.html', {'spisok_id': spisok_id, 'all_tasks': task})


def delete_spisok(request, del_id):
    spisok_to_delete = SpisokModel.objects.get(id=del_id)
    # SpisokModel.objects.remove(spisok_to_delete)
    spisok_to_delete.delete()
    all_spisok_names = SpisokModel.objects.filter()
    # .exclude(id=del_id)
    # all_spisok_names.remove(spisok_to_delete)
    # all_spisok_names.(spisok_to_delete)
    return render(request, 'Api/spisok.html',
                  {'spisok_name': [s.dict() for s in all_spisok_names]})
    # return render(request, 'Api/false.html')


def add_tasks(request, spisok_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # return render(request, 'Api/tasks.html')
            task_name = form.cleaned_data['task_name']
            TaskModel.objects.create(task_name=task_name)

            # return render(request, 'Api/tasks.html',
            #               {'task_name': [s.dict() for s in all_tasks]})
            return redirect(f'/tasks/{spisok_id}/')
        return render(request, 'Api/false.html')
    return render(request, 'Api/false.html')
    # return render(request, 'Api/tasks.html', {'add_task': ['das', '\dsadsa', '2321q']})
