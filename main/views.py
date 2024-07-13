from django.shortcuts import render, redirect
from . models import Banner, Address, Center_about, Staff,Student
def main(request):
    addres = Address.objects.all()
    banner = Banner.objects.all()
    c_about = Center_about.objects.all()
    
    
    
    context = {
        'banners': banner,
        'addresses': addres,
        'c_abouts': c_about,
        
    }
    
    if request.method == 'POST':
        f_name = request.POST["f_name"]
        phone = request.POST["Telefon"]
        email = request.POST["Pochta"]
        messege = request.POST["Xabarlaringiz"]
       
        Address.objects.create(
            f_name=f_name,
            phone=phone,
            email=email,
            messege=messege,
        )
        
        
        return render(request, 'index.html', context)
    
    return render(request, 'index.html', context)


def index(request):
    staff  = Staff.objects.all()
    student = Student.objects.all()
    context= {
        'staff_members' : staff,
        'students': student
    }
    return render(request, 'staff.html', context)