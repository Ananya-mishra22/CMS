from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from Home.models import classroom_booked,feedback,dt,is_student,complaint
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    user=request.user
    print(user)
    if user.is_authenticated:
        return render(request , 'home.html')

def faculty_signup(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrim password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            is_student.objects.create(username=uname,student='No')
            return redirect('facultysignin')
    return render(request,'signup.html')


def student_signup(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrim password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            is_student.objects.create(username=uname,student='Yes')
            return redirect('studentsignin')
    return render(request,'studentsignup.html')

def faculty_signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username, password=password)
        print(username,password)
        print(user)
        if user is not None:
            is_student_instance = is_student.objects.filter(username=username).last()
            if is_student_instance.student == "No":
                login(request,user)
                return redirect('Home')
            else:
                return HttpResponse ("You are not a faculty!!!")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Signin.html')


def student_signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username, password=password)
        print(username,password)
        print(user)
        if user is not None:
            is_student_instance = is_student.objects.filter(username=username).last()
            if is_student_instance.student == "Yes":
                login(request,user)
                return redirect('Home')
            else:
                return HttpResponse ("You are not a student!!!")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Signin.html')

def services(request):
    return render(request,'services.html')


@login_required
def contact(request):
    user=request.user
    print(user)
    if user.is_authenticated:
        return render(request,'contact.html')

@login_required
def floor_buttons(request):
    user=request.user
    print(user)
    if user.is_authenticated:
        floors = [1, 2, 3,4,5]  # Define your floors here
        return render(request, 'floor_buttons.html', {'floors': floors})

@login_required
def classroom_buttons(request, floor):
    user=request.user
    print(user)
    if user.is_authenticated:
        classrooms = {
            1: ['101', '102', '103'],
            2: ['201', '202', '203'],
            3: ['301', '302', '303'],
            4: ['401', '402', '403'],
            5: ['501', '502', '503']
            # Define classrooms for each floor
        }
        today_date = datetime.now().date()
        current_time = datetime.now().time()

        booked_classrooms = []

        # Iterate over classrooms for the given floor
        for classroom in classrooms[int(floor)]:
            # Check if there's a booking for the classroom
            if classroom_booked.objects.filter(c_no=classroom).exists():
                # Fetch the relevant booking for the classroom
                booking = classroom_booked.objects.filter(c_no=classroom).last()
                # Fetch the datetime record for the classroom's booking
                classroom_dt = dt.objects.filter(c_no=classroom,c_date=today_date).last()
                print(classroom)
                if classroom_dt:
                    
                    booking_datetime = datetime.combine(classroom_dt.c_date, classroom_dt.c_time)
                    # Calculate booking end time by adding the booked time duration
                    booking_end_time = booking_datetime + timedelta(minutes=booking.time)
                    print(classroom)
                    print("Booking datetime:", booking_datetime)
                    print("Booking end time:", booking_end_time)
                    print("Today's date:", today_date)
                    print("Current time:", current_time)
                    if booking_datetime <= datetime.combine(today_date, current_time) <= booking_end_time:
                        booked_classrooms.append(classroom)
                        print(classroom)
        print(booked_classrooms)
        lenbc=len(booked_classrooms)
        context = {
            'classrooms': classrooms[int(floor)],
            'booked_classrooms': booked_classrooms,
            'lenbc':lenbc
        }
        return render(request, 'classroom_buttons.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

@login_required
def person_form(request,classroom):
    user=request.user
    print(user)
    if user.is_authenticated:
        is_student_instance = is_student.objects.filter(username=user).last()
        if is_student_instance.student == "Yes":
            classrooms = {
                1: [101, 102, 103],
                2: [201, 202, 203],
                3: [301, 302, 303],
                4: [401, 402, 403],
                5: [501, 502, 503]
                # Define classrooms for each floor
            }
            print(classroom)
            # Determine floor based on classroom
            for floor, classrooms_in_floor in classrooms.items():
                print(classroom)
                if classroom in classrooms_in_floor:
                    break  # Found the floor, exit loop
            
            # Check if classroom is not found in any floor
            else:
                return HttpResponse("Classroom not found")

            context = {
                'floor': floor,
                'classroom': classroom,
            }
            if request.method == 'POST':
                name=request.POST.get('name')
                sname=request.POST.get('sname')
                time=request.POST.get('colorTime')
                print(name,sname,time)
                classroom_booked.objects.create(c_no=classroom,name=name,sname=sname,time=time)
                dt.objects.create(c_no=classroom,c_date=datetime.now().date(),c_time=datetime.now().time())
                return redirect('classroom_buttons', floor=floor)
            return render(request, 'form2.html',context)
        else:
            classrooms = {
                1: [101, 102, 103],
                2: [201, 202, 203],
                3: [301, 302, 303],
                4: [401, 402, 403],
                5: [501, 502, 503]
                # Define classrooms for each floor
            }
            print(classroom)
            # Determine floor based on classroom
            for floor, classrooms_in_floor in classrooms.items():
                print(classroom)
                if classroom in classrooms_in_floor:
                    break  # Found the floor, exit loop
            
            # Check if classroom is not found in any floor
            else:
                return HttpResponse("Classroom not found")

            context = {
                'floor': floor,
                'classroom': classroom,
            }
            if request.method == 'POST':
                name=request.POST.get('name')
                sname=request.POST.get('sname')
                time=request.POST.get('colorTime')
                print(name,sname,time)
                classroom_booked.objects.create(c_no=classroom,name=name,sname=sname,time=time)
                dt.objects.create(c_no=classroom,c_date=datetime.now().date(),c_time=datetime.now().time())
                return redirect('classroom_buttons', floor=floor)
            return render(request, 'form.html',context)

@login_required
def submit_form(request,classroom):
    user=request.user
    print(user)
    if user.is_authenticated:
        cb=classroom_booked.objects.filter(c_no=classroom).last()
        return render(request, 'form1.html',{'cb': cb})

@login_required
def classroom_form(request):
    user=request.user
    print(user)
    if user.is_authenticated:
            if request.method == 'POST':
                c_no=request.POST.get('c_no')
                text=request.POST.get('text')
                fb1=request.POST.get('Feedback')
                if fb1=='Yes':
                    complaint.objects.create(uname=user,c_no=c_no,text=text,status='Pending')  
                else:
                    print(c_no,text)
                    feedback.objects.create(uname=user,c_no=c_no,text=text)
            co = complaint.objects.all()
            fb = feedback.objects.all()
            context = {
                'fb': fb,
                'co': co,
                }
            return render(request, 'classroom_form.html',context)
  
