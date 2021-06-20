import datetime
import time as t
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Todo

# Create your views here.
def home(request, *args, **kwargs):
    context = {'title': 'Home',}
    return render(request, 'mainapp/home.html', context)

def signup(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account for {user} has been created!')
                return redirect('/login')
        context = {'title': 'Sign Up', 'form': form}
        return render(request, 'mainapp/signup.html', context)

def loginform(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Incorrect credentials!')
            
        context = {'title': 'Login',}
        return render(request, 'mainapp/login.html', context)

@login_required(login_url='/login')
def logoutuser(request, *args, **kwargs):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def dashboard(request, *args, **kwargs):
    context = {'title': 'Dashboard', 'main_data': False}
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['desc']
        language = request.POST['lang-drp']
        category = request.POST['cat-drp']
        time = request.POST['time-in']
        date = request.POST['date-in']
        user = request.user.username
        Todo.objects.create(title=title, description=description, language=language, category=category, time=time, deadline=date, user=user)
        messages.success(request, '1')
        return redirect('/dashboard')
    
    return render (request, 'mainapp/dashboard.html', context)

@login_required(login_url='/login')
def editprofile(request, *args, **kwargs):
    u_form = UserUpdateForm()
    if request.method == 'POST':
        main = Todo.objects.filter(user=request.user.username)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            username = u_form.cleaned_data['username']
            main.update(user=request.user.username)
            u_form.save()
            messages.success(request, 'Your profile has been updated!')
        else:
            messages.error(request, 'Invalid update credentials!')
    context = {'title': 'Edit Profile', 'form': u_form}
    return render(request, 'mainapp/editprofile.html', context)

@login_required(login_url='/login')
def taskedit(request, *args, **kwargs):
    obj = Todo.objects.filter(user=request.user)
    date_year = datetime.datetime.now().year
    if datetime.datetime.now().month < 10:
        date_month = f'0{datetime.datetime.now().month}'
    else:
        date_month = datetime.datetime.now().month
    date_date = datetime.datetime.now().date

    #Error code above
    
    main_date = str(datetime.date.today()).replace('-', ' ').split()
    context = {'title': 'Edit and View Tasks', 'obj': obj, 'year': int(main_date[0]), 'month': int(main_date[1]), 'date': int(main_date[2])}
    return render(request, 'mainapp/edit.html', context)

@login_required(login_url='/login')
def delete(request, *args, **kwargs):
    if request.method == 'POST':
        id = Todo.objects.get(id=request.POST.get('delete-input'))
        id.delete()
        messages.info(request, 'del')
    return redirect('/task')

@login_required(login_url='/login')
def task_mod(request, *args, **kwargs):
    if request.method == 'POST':
        main_id = request.POST['id-input']
        if request.POST['select-edit'] == 't':
            if request.POST['title-input'] != '' and request.POST['desc-input'] != '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.title = request.POST['title-input']
                updatefield.description = request.POST['desc-input']
                updatefield.save()
                messages.success(request, 'up')
                
            elif request.POST['title-input'] == '' and request.POST['desc-input'] != '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.description = request.POST['desc-input']
                updatefield.save()
                messages.success(request, 'up')
                
            elif request.POST['title-input'] != '' and request.POST['desc-input'] == '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.title = request.POST['title-input']
                updatefield.save()
                messages.success(request, 'up')
            else:
                pass
            
        elif request.POST['select-edit'] == 'c':
            if request.POST['category'] != 'Edit Category *' and request.POST['language'] != 'Edit Development Language *':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.category = request.POST['category']
                updatefield.language = request.POST['language']
                updatefield.save()
                messages.success(request, 'up')
                
            else:
                pass
            
        elif request.POST['select-edit'] == 'd':
            if request.POST['time-edit'] != '' and request.POST['date-edit'] != '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.time = request.POST['time-edit']
                updatefield.deadline = request.POST['date-edit']
                updatefield.save()
                messages.success(request, 'up')
                
            elif request.POST['time-edit'] == '' and request.POST['date-edit'] != '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.deadline = request.POST['date-edit']
                updatefield.save()
                messages.success(request, 'up')
                
            elif request.POST['time-edit'] != '' and request.POST['date-edit'] == '':
                updatefield = Todo.objects.get(id=main_id)
                updatefield.time = request.POST['time-edit']
                updatefield.save()
                messages.success(request, 'up')
                
            else:
                pass
            
    return redirect('/task')

@login_required(login_url='/login')
def taskitem(request, *args, **kwargs):
    kitem_id = kwargs['key']
    user_instance = Todo.objects.filter(user=request.user.username)
    try:
        data = user_instance.get(id=kitem_id)
    except Exception:
        return redirect('/task')
    context = {'title': 'Task Details', 'data': data,}
    return render(request, 'mainapp/items.html', context)

@login_required(login_url='/login')
def finditem(request, *args, **kwargs):
    if request.method == 'POST':
        item_id = request.POST['search_bar']
        return redirect(f'/item/{item_id}')
    else:
        return redirect('/task')
    
    
    