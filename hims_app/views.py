from django.shortcuts import render, redirect
from django.http import HttpResponse
from hims_app.models import Customers, Rooms, Bookings
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboardView(request):
    no_of_cust = Customers.objects.all().count()
    no_of_rooms = Rooms.objects.all().count()
    no_of_bookings = Bookings.objects.all().count()
    dict = {'c_cust': no_of_cust,
            'c_room': no_of_rooms, 'c_books': no_of_bookings}
    return render(request, 'hims_app/dashboard.html', dict)

############# ROOM SECTION ###########################

@login_required
def roomview(request):
    rooms = Rooms.objects.all()
    dict = {'rooms': rooms}
    return render(request, 'hims_app/rooms.html', dict)

@login_required()
def addroomview(request):
    if request.method == 'POST':
        if (request.POST.get('room_name') and 
            request.POST.get('room_available_for') and
            request.POST.get('room_type') and
            request.POST.get('room_charges')):

            rn = request.POST.get('room_name')
            raf = request.POST.get('room_available_for')
            rt = request.POST.get('room_type')
            rc = request.POST.get('room_charges')
    
            room_instance = Rooms()
            room_instance.room_name = rn
            room_instance.room_available_for = raf
            room_instance.room_type = rt
            room_instance.room_charges = rc
            room_instance.save()
            messages.success(request, 'room added')
            return redirect('rooms')
        else:
            messages.error(request, "All fields are required")
            return redirect('rooms')
      
    else:
        return redirect('rooms')

@login_required
def updateroomview(request, room_id):
    if request.method == "POST":
        if (request.POST.get('room_name') and
                request.POST.get('room_available_for') and
                request.POST.get('room_type') and
                request.POST.get('room_charges')):
            # update
            Rooms.objects.filter(id=room_id).update(
                room_name=request.POST.get('room_name'),
                room_available_for=request.POST.get('room_available_for'),
                room_type=request.POST.get('room_type'),
                room_charges=request.POST.get('room_charges')
            )
            messages.success(request, "room updated successfully")
            return redirect('rooms')
        else:
            messages.error(request, "Error updating the course")
            return redirect('rooms')
    else:
        redirect('rooms')

@login_required
def deleteroomview(request, room_id):
    if request.method == "POST":
        Rooms.objects.filter(id=room_id).delete()
        # message here
        messages.warning(request, "room deleted")
        return redirect('rooms')
    else:
        return redirect('rooms')

####### END ROOM SECTION ##########

@login_required
def customersview(request):
    customers = Customers.objects.all()
    dict = {'customers': customers}
    return render(request, 'hims_app/customers.html', dict)

@login_required
def addcustomerview(request):
    if request.method == 'POST':
        # check if any if the fields is empty
        if (request.POST.get('First_Name') and
                request.POST.get('Last_Name') and
                request.POST.get('Surname') and
                request.POST.get('Email') and
                request.POST.get('Phone_Number')
            ):
            fname = request.POST.get('First_Name')
            lname = request.POST.get('Last_Name')
            surname = request.POST.get('Surname')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone_Number')

            # GENERATE CUSTOMER BOOK NO # HOT/2020/1
            year = date.today().year

            lastcustomer = Customers.objects.last()

            if lastcustomer:
                NewcustomerId = lastcustomer.id + 1
            else:
                NewcustomerId = 1

            custno = "HOT/" + str(year) + '/' + str(NewcustomerId)

            try:
                customer = Customers()
                customer.cust_no = custno
                customer.First_Name = fname
                customer.Last_Name = lname
                customer.Surname = surname
                customer.Email = email
                customer.Phone_Number = phone
                customer.save()
                messages.success(request, "customer Added")
                return redirect('customers')
            except Exception:
                messages.error(request, "Failed to add customer")
                return redirect('customers')
        else:
            # message here
            pass
    else:
        return redirect('customers')

@login_required
def updatecustomerview(request,customer_id):
    if request.method == 'POST':
        # check if any if the fields is empty
        if (request.POST.get('First_Name') and
            request.POST.get('Last_Name') and
            request.POST.get('Surname') and
            request.POST.get('Email') and
            request.POST.get('Phone_Number')
            ):
            Customers.objects.filter(id=customer_id).update(
                First_Name=request.POST.get('First_Name'),
                Last_Name=request.POST.get('Last_Name'),
                Surname=request.POST.get('Surname'),
                Email=request.POST.get('Email'),
                Phone_Number=request.POST.get('Phone_Number')
            )
            messages.success(request, "customer Updated")
            return redirect('customers')
        else:
            messages.error(request, "Error Updating customer")
            return redirect('customers')
    else:
        return redirect('customers')

@login_required
def deletecustomerview(request,customer_id):
    if request.method == "POST":
        Customers.objects.filter(id=student_id).delete()
        # message here
        messages.warning(request, "customer deleted")
        return redirect('customers')
    else:
        return redirect('customers')

@login_required
def bookingsview(request):
    bookings = Bookings.objects.all()
    dict = {'bookings': bookings}
    return render(request, 'hims_app/bookings.html', dict)


# #### Admin authicatication #####
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "Logged In")
                return redirect('dashboard')
            else:
                messages.warning(request, "Your account has been deactivated")
                return render(request, 'registration/adminlogin.html')

        else:
            messages.error(request, "Invalid login credentials")
            return render(request, "registration/adminlogin.html")
    else:
        return render(request, "registration/adminlogin.html")


def admin_logout(request):
    logout(request)
    messages.warning(request, "logged out")
    return redirect('admin-login')

# frontend


def homepageview(request):
    return render(request, ('frontend/home.html'))


def displayrooms(request):
    rooms = Rooms.objects.all()
    dict = {'rooms': rooms}
    return render(request, ('frontend/viewrooms.html'), dict)
