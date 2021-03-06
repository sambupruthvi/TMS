from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Project, TimeSheet
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
import datetime
# Create your views here.
def login_view(request):
    print('in the login view')
    if request.method == 'POST':
        print('POST')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data = {
                'logged_in': True,
                 'send_to' : 'accounts/profile.html'
            }
            username = User.objects.get(username=request.user.username)
            profile = Profile.objects.filter(user=username)
            return render(request, 'accounts/profile.html', {'profile': profile[0]})
            #return JsonResponse(data)
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect'})
    else:
        return render(request, 'accounts/login.html')



"""check if the user is is_authenticated
else render the login page
if logged in send him the projects he is involved in."""
def project_view(request):
    if request.user.is_authenticated:
        id = request.user.id
        emp_profile = Profile.objects.filter(user=id)[0] # get the profile object of the logged in user
        projects = emp_profile.project_set.all()         # use the profile object to get his projects
        return render(request, 'accounts/project.html', {'projects':projects})
    else:
        return render(request, 'accounts/login.html', {'error': 'Login to access the page'})

# Checks if the user is logged in, else return him/her to login page
def timesheet_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user)[0]
        print(profile)
        timesheets = TimeSheet.objects.filter(profile=profile)
        print(timesheets)
        return render(request, 'accounts/timesheet.html', {'timesheets':timesheets})
    else:
        return render(request, 'accounts/login.html', {'error': 'Login to access the page'})

"""check if the user is logged in else return him to the login page
if request.method is GET send him the accounts/add_timesheet.html which has the form
to submit new TimeSheet
if request.method is POST write the timesheet object received to the database"""
def add_timesheet(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            project_id = request.POST.get('project_id')
            project = Project.objects.filter(id=project_id)[0]
            if request.POST['from'] >= request.POST['to']:
                return render(request, 'accounts/add_timesheet.html', {'project':project,'error':'start time should be less than end time'})
            profile = Profile.objects.filter(user=request.user)[0]
            added_timesheets = TimeSheet.objects.filter(profile=profile)
            #print(added_timesheets)
            for t in added_timesheets:
                a = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
                if t.date == a:
                    print(t.date, request.POST['date'])
                    if t.start_time <= datetime.datetime.strptime(request.POST['from'], '%H:%M').time()  < t.end_time or t.start_time < datetime.datetime.strptime(request.POST['to'], '%H:%M').time() <= t.end_time:
                        return render(request, 'accounts/add_timesheet.html', {'project':project,'error':'Conflit in adding new timesheet'})
            timesheet = TimeSheet()
            timesheet.date = request.POST['date']
            timesheet.start_time = request.POST['from']
            timesheet.end_time = request.POST['to']
            timesheet.project = Project.objects.filter(id=request.POST.get('project_id'))[0]
            timesheet.emp_name = request.user.username
            timesheet.save()
            #profile = Profile.objects.filter(user=request.user)[0]
            timesheet.profile.add(profile)
            timesheet.save()
            id = request.user.id
            print(timesheet.profile, request.user)
            emp_profile = Profile.objects.filter(user=id)[0] # get the profile object of the logged in user
            projects = emp_profile.project_set.all()         # use the profile object to get his projects
            return render(request, 'accounts/project.html', {'projects':projects})
        else:
            project_id = request.GET.get('project_id')
            project = Project.objects.filter(id=project_id)[0]
            return render(request, 'accounts/add_timesheet.html', {'project':project})
    else:
        return render(request, 'accounts/login.html', {'error': 'Login to access the page'})

"""check if the user is logged in else return him to the login page
if the request.method is GET, get the timesheet the user requested from database
check if the grace days are no more than 14 days. if more than 14 days send him/her to previous page
with an error messaage
if not then send him the requested timesheet to be edited."""
def edit_timesheet(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            timesheet_id = request.POST.get('timesheet_id')
            timesheet = TimeSheet.objects.filter(id=timesheet_id)[0]
            timesheet.user = request.user.username
            timesheet.date = request.POST['date']
            timesheet.start_time = request.POST['from']
            timesheet.end_time = request.POST['to']
            project = Project.objects.filter(project_name = request.POST.get('project_name'))[0]
            timesheet.project = project
            timesheet.save()
            profile = Profile.objects.filter(user=request.user)[0]
            timesheets = TimeSheet.objects.filter(profile=profile)
            return render(request, 'accounts/timesheet.html', {'timesheets':timesheets})
        else:
            timesheet_id = request.GET.get('timesheet_id')
            timesheet = TimeSheet.objects.filter(id=timesheet_id)[0]
            """if the requested timesheet's date to be edited is before 2 weeks
            then return the timesheets apge to user saying that, he canot edit that timesheet."""
            date = datetime.date.today()
            start_week = date - datetime.timedelta(date.weekday()+7)
            end_week = start_week + datetime.timedelta(14)
            if start_week <= timesheet.date < end_week:
                return render(request, 'accounts/edittimesheet.html', {'timesheet':timesheet})
            profile = Profile.objects.filter(user=request.user)[0]
            timesheets = TimeSheet.objects.filter(profile=profile)
            return render(request, 'accounts/timesheet.html', {'error':'You can\'t edit your two weeks past timesheet', 'timesheets':timesheets})
    else:
        return render(request, 'accounts/login.html', {'error': 'Login to access the page'})

# check if the user is logged in else return him to the login page
# get the profile object of the user and send it to him/her.
def profile_view(request):
    if request.user.is_authenticated:
        username = User.objects.get(username=request.user.username)
        profile = Profile.objects.filter(user=username)
        return render(request, 'accounts/profile.html', {'profile':profile[0]})
    else:
        return render(request, 'accounts/login.html', {'error': 'Login to access the page'})



def logout_view(request):
    logout(request)
    return render(request, 'accounts/login.html', {'error':'logged out succesfully'})