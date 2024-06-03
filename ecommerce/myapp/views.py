from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages, auth
from rest_framework.authtoken.models import Token

from .forms import SignupForm
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

def testing(request):
    return render(request, 'addtask.html')
# Create your views here.

class ListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if request.method == "GET":
            tasks = Task.objects.filter(user=request.user)
            serializer = TaskSerializer(tasks, many=True)
            context = {
                'serializer':serializer
            }
            return render(request, 'index.html', context)
        


def post_todo(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.method == "POST":
        task_name = request.POST['task_name']
        description = request.POST['description']
        task = Task.objects.create(task_name=task_name, description=description, user=request.user)
        if task is not None:
            return redirect('index')


        
    return render(request, 'addtask.html')
        
        
@api_view(['PUT'])
def update_todo(request, pk):
    if request.method == "PUT":
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


def delete_todo(request, pk):
    
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')

def mark_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect('index')

def completed_task(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        tasks = Task.objects.filter(is_completed=True)
        serializer = TaskSerializer(tasks, many=True)
        context = {
        'serializer':serializer
        }
        return render(request, 'completed_task.html', context)

    
   
    


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request, "You signed up successfully!")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = SignupForm()

    context = {
        'form':form
    }

    return render(request, 'signup.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password  = request.POST.get('password')

        if username is None or password is None:
            return Response("Username or password is not provided!!")
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # token, _ = Token.objects.get_or_create(user=user)
            messages.success(request, "Logged in successfully!!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, 'login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
  # Log out the user
  logout(request)
  # Redirect to a specific page (optional)
  return redirect('login') 
        







       
