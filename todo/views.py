from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt


def home(request):
    not_completed = models.Task.objects.filter(
        completed=False).order_by("-completed_at")
    completed = models.Task.objects.filter(
        completed=True).order_by("-completed_at")
    return render(request, 'todo/index.html', {
        'not_completed': not_completed,
        'completed': completed
    })


@csrf_exempt
def add_todo(request):
    text = request.POST.get('title')
    completed = False
    models.Task.objects.create(title=text, completed=completed)
    return HttpResponseRedirect('/')


def mark_as_complete(request, todo_id):
    completed = True
    models.Task.objects.filter(id=todo_id).update(completed=completed)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    models.Task.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')


@csrf_exempt
def edit_todo(request, todo_id):
    todo = models.Task.objects.get(id=todo_id)
    return render(request, 'todo/update.html', {'todo': todo})


@csrf_exempt
def update_todo(request, todo_id):
    title = request.POST.get('title')
    models.Task.objects.filter(id=todo_id).update(title=title)
    return HttpResponseRedirect('/')
