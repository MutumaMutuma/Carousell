from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Carousell account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for Joining Carousel. Now you can now <a href="/accounts/login/">Login</a> your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def index(request):
    date = dt.date.today()
    items = Item.objects.all()
    return render(request, 'index.html',{"date":date, "items":items})

def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    
    return render(request, 'profile/profile.html', {"date": date, "profile":profile})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})

@login_required(login_url='/accounts/login/')
def new_sell(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            sell = form.save(commit=False)
            sell.user = current_user
            sell.seller = request.user
            sell.save()
        return redirect('index')

    else:
        form = ItemForm()
    return render(request, 'new_sell.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categorys = Category.objects.filter(category=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all()
      
        return render(request, 'search.html',{"message":message,"category": searched_categorys,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def items(request,id):
    date = dt.date.today()
    posts=Item.objects.get(id=id)
    return render(request,'each_item.html',{"posts":posts,"date":date})