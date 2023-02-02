from django.shortcuts import render,get_object_or_404
from django.http import Http404
from todo.models import Todo,Category,Tag
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='admin/login/')
def home_view(request):
    todos = Todo.objects.filter(is_active = True,user=request.user)
    context = dict(
        todos=todos,
    )
    return render(request,"todo/todo_list.html",context)

@login_required(login_url='admin/login/')
def todo_detail_view(request,id,category_slug):   
    todo = get_object_or_404(Todo,pk=id,category__slug=category_slug,user=request.user)
    tag = Tag.objects.filter(todo=todo)
    context = dict(
    todo=todo,
     tag=tag,)
    return render(request,"todo/todo_detail.html",context)

@login_required(login_url='admin/login/')
def category_detail_view(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug,)    
    todos = Todo.objects.filter(is_active = True,category=category,user=request.user)
    context = dict(
        todos=todos,
        category=category,
       
    )
    return render(request,"todo/todo_list.html",context)
    
@login_required(login_url='admin/login/')
def tag_view(request,tag_slug):
    tag = get_object_or_404(Tag,slug=tag_slug,)    
    context = dict(
        tag=tag,
        todos=tag.todo_set.filter(user=request.user),        
    )
    return render(request,"todo/todo_list.html",context)


