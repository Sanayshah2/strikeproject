from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# from django.db.models import Q
from django.utils import timezone
# from .decorators import *

# Create your views here.
def home(request):
    # categories=get_all_help_categories()
    # requirements = Requirement.objects.all()

    # context={
    #     'requirements':requirements,
    #     'categories':categories,
        
    # }


    return render(request,'Client/home.html')

def register(request):
    if request.method=='POST':
      form1=UserForm(request.POST)
      form2 = ClientForm(request.POST)
      if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            passw = form1.cleaned_data.get('password1')
            user = User.objects.get(username = username)
            instance = form2.save(commit=False)
            instance.user = user
            instance.save()
            udata = UserData(username = username, password = passw)
            udata.save()
            # group = request.POST.get('group')
            # group1 = Group.objects.get(name = group)
            # user = form.save(commit=False)
            # user.groups.add(group1)
            # user.save()
            # if group == 'ngo':
            #     ngo = Ngo(user=user)
            #     ngo.save()
            # else:
            #     donor = Donor(user=user)
            #     donor.save()

            return redirect('login')    
    else:
      form1=UserForm()
      form2 = ClientForm()
    return render(request,'Client/register.html',{'userform':form1, 'clientform':form2})

# @is_logged
def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            if user is not None:

                # group=Group.objects.get(user=user)
                # g=group.name
                # if g == 'donor':
                #   login(request, user)
                #   return redirect('donorDashboard')
                # else:
                #   login(request, user)
                #   return redirect('ngoDashboard')
                login(request, user)
                return redirect('ClientDashboard')

            elif user is None:
                messages.info(request, f'Invalid Credentials.')
    else:
        form= LoginForm()
    return render(request,"Client/login.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

# @login_required
# @donor_required
# def donorDashboard(request):
#    return redirect('home')

def ClientDashboard(request):
    # ngo=Ngo.objects.get(user=request.user)
    # requirements=Requirement.objects.filter(ngo=ngo)
    # context={
    #     'requirements':requirements,
    # }
    client=Client.objects.get(user=request.user)
    count1=Count_table.objects.filter(user = request.user.username).last()
    orders=list(Order.objects.filter(client=client))
    checked_val='i'
    if client.auto_order == True:
        checked_val='checked'
    
    print(orders)
    tq=0
    for x in orders:
        tq=tq+x.quantity
    print(tq)
    context={
        'client':client,
        'count1':count1,
        'tq':tq,
        'dashboard':'active',
        'checked': checked_val

    }

    return render(request,'Client/ngo_dashboard.html',context)

def OrderHistory(request):
    
    orders=Order.objects.filter(client = Client.objects.get(user = request.user))
    context={
        'orders':orders,
        'orderHistory':'active'
    }

    return render(request,'Client/order_history.html',context)

def addOrder(request):
    # categories= get_all_help_categories()
    if request.method=='POST':
        # ngo=Ngo.objects.get(user=request.user)
        # print(ngo)
        # category=request.POST.get('category')
        # print(category)



        # category1=Help_category.objects.get(help_category = category)
        
        form=AddOrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)

            # if category == 'Financial':
            #     amount=request.POST.get('amount')
            #     instance.amount=amount
            # else:
            #     quantity=request.POST.get('quantity')
            #     instance.quantity=quantity

            # #print(category1)
            # instance.category=category1
            client = Client.objects.get(user = request.user)
            instance.client = client
            instance.save()
            messages.info(request, f"Order Added.")
            return redirect('addOrder')
        else:
            messages.info(request, f"Error occured, Try again.")
    else:
        form=AddOrderForm()
    return render(request,'Client/addOrder.html',{'form':form,'addOrder':'active'})


def AutoOrder(request):

    if request.method=='POST':
        client=Client.objects.get(user=request.user)
        if client.auto_order==True:
            client.auto_order=False
        else:
            client.auto_order=True


        
        client.save()
        return redirect('ClientDashboard')




