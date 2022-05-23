from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect

from TaskManager.models import Task


def dashboard(request):
    total_tasks = Task.objects.all().count()
    completed = Task.objects.filter(is_completed=True).count()
    pending = Task.objects.filter(is_completed=False).count()
    revenue = Task.objects.filter(cost__isnull=False).aggregate(Sum("cost"))
    context = {
        "total_tasks": total_tasks,
        "pending": pending,
        "completed": completed,
        "revenue": revenue,
    }
    return render(request, template_name="dashboard.html", context=context)


def create_task(request):
    if request.method == "POST":
        task = Task.objects.create(
            task_name=request.POST.get("task_name"),
            task_desc=request.POST.get("task_desc"),
            cost=request.POST.get("cost"),
            start_date=request.POST.get("start_date"),
            due_date=request.POST.get("due_date"),
        )
        task.save()
        messages.success(request, "Task Created Successfully!")
    return render(request, template_name="tasks/create.html")


def all_tasks(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, template_name="tasks/tasks.html", context=context)


def mark_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect("all_tasks")


def delete_task(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return redirect("all_tasks")
