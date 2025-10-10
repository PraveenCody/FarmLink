# Create your views here.
from django.shortcuts import render,redirect
from .models import Users,Farmer,AllProducts
from django.contrib import messages
from django.contrib.auth import logout

def main(request):
    return render(request, 'main.html')

def uregister(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']

        # Create user
        user = Users(name=fullname,email=email,mobile=mobile,address=address,password=password)
        user.save()
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('ulogin')

    return render(request, 'uregister.html')

def fregister(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        village = request.POST['village']
        password = request.POST['password']
        aadharno = request.POST['aadharno']

        # Create user
        user = Farmer(name=fullname,email=email,mobile=mobile,address=address,
                                          village=village,password=password,
                                          aadharno=aadharno)
        user.save()
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('flogin')

    return render(request, 'fregister.html')

def ulogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        duser = Users.objects.filter(email=email,password=password)
        if duser.exists():
            return redirect('uindex')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'ulogin.html')


def flogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        duser = Farmer.objects.filter(email=email,password=password)
        if duser.exists():
            farmer = duser.first()  # get the first matched farmer
            request.session['farmer_email'] = email
            request.session['fids'] = farmer.fid
            return redirect('findex')  # your farmer dashboard page
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'flogin.html')

def uindex(request):
    products = AllProducts.objects.all()
    return render(request,'uindex.html',{'products':products})

def findex(request):
    if 'farmer_email' not in request.session:
            return redirect('flogin')

    fids = request.session['fids']
    farmer = Farmer.objects.filter(fid=fids)
    
    products = AllProducts.objects.filter(fid=fids)

    return render(request,'findex.html', {'products': products,'farmer':farmer})
    
def upload_product(request):
    if request.method == 'POST':
        farmer_email = request.session['farmer_email']
        farmer = Farmer.objects.get(email=farmer_email)

        farmer_location = request.POST['farmer_location']
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        cultivated_date = request.POST['cultivated_date']
        experiry_date = request.POST['experiry_date']
        photo = request.FILES['photo']  # get the uploaded file

        AllProducts.objects.create(
            fid=farmer.fid,
            farmer_name=farmer.name,
            farmer_location=farmer_location,
            product_name=product_name,
            product_description=product_description,
            cultivated_date=cultivated_date,
            experiry_date=experiry_date,
            photo=photo  
        )

        messages.success(request, "✅ Product uploaded successfully!")
        return redirect('findex')

    return render(request, 'uploads.html')

def log_out(request):
    logout(request)
    return redirect('/')