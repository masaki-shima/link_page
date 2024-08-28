from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView
from todo_list.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        searchInputText = self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(title__icontains=searchInputText)
        
        context["search"] = searchInputText
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"] #["user", "title", ....... ]
    success_url = reverse_lazy("todo_list:tasks")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__" #["user", "title", ....... ]
    success_url = reverse_lazy("todo_list:tasks")

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__" #["user", "title", ....... ]
    success_url = reverse_lazy("todo_list:tasks")
    context_object_name = "task"
    
class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todo_list/login.html"
    
    def get_success_url(self):
        return reverse_lazy("todo_list:tasks")
    
class RegisterTodoApp(FormView):
    template_name = "todo_list/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("todo_list:tasks")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
            