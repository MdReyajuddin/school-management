from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from schooladmin.forms import StudentsForm, IndexForm, ContactForm, LoginForm
from schooladmin.models import Staffs, Departments, Classes, Students, Index



# Create your views here.
#Signup & Login,Logout,Password Reset used by auth models
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Signed')
            return students_data(request)
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



#CRUD operation for student details

def index(request):
    allstud = Students.objects.all()
    alldepart = Departments.objects.all()
    allstaff = Staffs.objects.all()
    allclass = Classes.objects.all()
    data = {'allstud': allstud, 'alldepart': alldepart, 'allclass': allclass, 'allstaff': allstaff}
    return render(request, 'index.html', {'data': data})



#To display all students details

def students_data(request):
    data = Students.objects.all().order_by('name')
    query= request.GET.get('q')
    if query:
        data = Students.objects.filter(
        Q(name__icontains=query)|
        Q(address__icontains=query)|
        Q(category__icontains=query)
        )
    paginator =Paginator(data, 2)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(data,index=4)
    page_range = list(paginator.page_range)[start_index:end_index]

    return render(request, 'student_alldata.html', {'data': data, 'page_range':page_range})

def proper_pagination(data,index):
    start_index = 0
    end_index = 7
    if data.number>index:
        start_index = data.number - index
        end_index = start_index + end_index
    return (start_index, end_index)



#To display a students details

def students_detail(request, id):
    data = Students.objects.get(id=id)
    return render(request, 'student_detail.html', {'data': data})





#To create students details

def students_create(request):
    form = StudentsForm()
    if request.method == "POST":
        data = StudentsForm(request.POST)
        if data.is_valid():
            data.save(commit=True)
        messages.success(request, 'Successfully Created')
        return students_data(request)
    return render(request, 'student_create.html', {'form': form})



#To update students details

def students_update(request, id):
    data = Students.objects.get(id=id)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=data)
        if form.is_valid():
            new=form.save(commit=False)
            new.save()
        messages.warning(request, 'Successfully Updated')
        return students_data(request)
    return render(request, 'student_update.html', {'data': data})



#To delete students details

def students_delete(request, id):
    data = Students.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        messages.warning(request, 'Successfully Deleted')
        return students_data(request)
    return render(request, 'student_delete.html', {'data': data})



#Home page details
def home_view(request):
    elem = Index.objects.get()
    return render(request, 'home_detail.html', {'elem': elem})



#home page edit

def home_edit(request):
    form = IndexForm()
    if request.method == "POST":
        data = IndexForm(request.POST)
        if data.is_valid():
            data.save(commit=True)
        messages.warning(request, 'Successfully Edited')
        return home_view(request)
    return render(request, 'home_create.html', {'form': form})



#Help page for contact
def help(request):
    form = ContactForm()
    if request.method == "POST":
        data = ContactForm(request.POST)
        if data.is_valid():
            data.save(commit=True)
        return students_data(request)
    return render(request, 'help.html', {'form': form})



#About Page
def about(request):
    return render(request, 'about.html')



#Calender Page
def calender(request):
    return render(request, 'calender.html')

#Authentications Starts Here
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is None')
    else:
        form= LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')
