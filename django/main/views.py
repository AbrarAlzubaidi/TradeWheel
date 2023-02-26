from imp import reload
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings

from users.models import Profile
from users.forms import LocationForm

from .models import Car, UsersLikedCars
from .forms import AddCarForm
from .filters import CarFilter
# create a view that responsible to show themain page that will appear when any user will navigate to the website

def main_view(request):
    """
    landing page when user navigates into the website
    that will return a http response
    """
    template_path = "main/main.html"
    return render(request, template_path, {"name": "automax"})
    # {"name": "automax"} this dictionary is for pass avalue to the template

@login_required
def home_page_view(request):
    """
    home page view when user logged in
    """
    car_list = Car.objects.all()
    car_list_filter = CarFilter(request.GET, queryset=car_list)

    user_id = request.user.id
    user_profile = Profile.objects.filter(user=user_id).get()

    liked_cars = UsersLikedCars.objects.filter(profile=user_profile).values_list('car')
    liked_cars_id = [car[0] for car in liked_cars]

    return render(request, "main/home.html", {
        "car_list":car_list, # if we keep this when we apply the filter the listing data still shown
        "car_list_filter":car_list_filter,
        "liked_cars_id": liked_cars_id
    })


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = AddCarForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()

                user_id = request.user.id
                # print('*'*50, user_id)
                user_profile = Profile.objects.filter(user=user_id).get()
                # print('*'*50, user_profile)

                listing.seller = user_profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, f'An error occured while posting the listing. {e}')
    elif request.method == 'GET':
        listing_form = AddCarForm()
        location_form = LocationForm()
        
    return render(request, 'main/create_car.html', {'listing_form': listing_form, 'location_form': location_form, })

    
@login_required
def detail(request, car_id): # car_id: is the name of the param
    data = get_object_or_404(Car, id=car_id)
    try:
        if data is None:
            raise Exception
        else:
            return render(request, 'main/car_detail.html', {'car':data})
        
    except Exception as e:
        messages.error(request, f'invalid UID passed {id} was not correct')
        return redirect('home')
    
@login_required
def edit_view(request, car_id):
    try:
        car = get_object_or_404(Car, id=car_id)
        if car is None:
            raise Exception
        
        if request.method == 'POST':
            listing_form = AddCarForm(request.POST, request.FILES, instance=car)
            location_form = LocationForm(request.POST, instance=car.location)

            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(
                        request, f'Updating Successfully!')
                return redirect('home')
            else:
                messages.error(request, 'an error happen when edit the data')
                return reload()
    
        else:
            listing_form = AddCarForm(instance=car)
            location_form = LocationForm(instance=car.location)
            return render(request, 'main/edit_car.html', {
                'location_form': location_form,
                'listing_form': listing_form,
            })
    
    except Exception as e:
        messages.error(request, f'an error happen when edit the data {e}')
        return redirect('home')

def liked_car_view(request, car_id):
    # get selected car by id
    car = get_object_or_404(Car, id=car_id)
    # get user profile that liked the car
    user_id = request.user.id
    user_profile = Profile.objects.filter(user=user_id).get()
    # create the link (instance) between the profile and the car
    liked_instance, created = UsersLikedCars.objects.get_or_create(profile=user_profile, car=car)# check if the like is exist (then get it), else, create the like relation. this function return 2 values: the instance and a boolean value to mark the operation if it is created or exist

    if created:
        # means user liked this car so add it to the relation
        liked_instance.save()
    else:
        # means their is a relation (user liked this car) so the user want to delete/unlike this car
        liked_instance.delete()

    return JsonResponse({
        "username": user_profile.user.username,
        "car_model": car.model,
        "liked": created
    })


def sending_email_view(request, car_id):
    """
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
    """
    car = get_object_or_404(Car, id=car_id)
    from_email = settings.EMAIL_HOST_USER  
    recipient_list = [car.seller.user.email,]
    message_subject = f'{request.user.username} is interested in your car {car.model}'
    message_body = f' Hi {car.seller.user.username}, {request.user.username} user is interested in your car which is {car.model} on Automax '  
    print('*'*50, from_email,'\n', recipient_list,'\n', message_subject,'\n', message_body)
    
    try:
        send_mail(message_subject, message_body, from_email, recipient_list, fail_silently=True)
        return JsonResponse({
            'success': True,
            'info': 'sending email successfully'
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "success": False,
            "info": e
        })

def send_email(request, car_id):  
   
   try: 
        with get_connection(  
                host=settings.EMAIL_HOST, 
                port=settings.EMAIL_PORT,  
                username=settings.EMAIL_HOST_USER, 
                password=settings.EMAIL_HOST_PASSWORD, 
                use_tls=settings.EMAIL_USE_TLS  
        ) as connection:
            print(car_id)
            car = get_object_or_404(Car, id=car_id)
            subject = f'{request.user.username} is interested in your car {car.model}'
            message = f' Hi {car.seller.user.username}, {request.user.username} user is interested in your car which is {car.model} on Automax '  
            email_from = settings.EMAIL_HOST_USER  
            recipient_list = [car.seller.user.email, ]  
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
        
        return JsonResponse({
                'success': True,
                'info': 'sending email successfully'
            })
   except Exception as e:
        return JsonResponse({
            "success": False,
            "info": e
        })

# @login_required
# def create_car(request):
#     if request.method == 'POST':
#         try:
#             create_form = AddCarForm(request.POST, request.FILES) # request.FILES: to get the media file cause the .POST did not get it 
#             location_form = LocationForm(request.POST)
#             if create_form.is_valid() and location_form.is_valid(): # if the car is vaild and the location form also then
#                 car = create_form.save(commit=False) # save the car info but dont commit it to the database yet
#                 #? why save the data but dont push it into the db? cause we have some data to grab it then we will save it
#                 location = location_form.save() # save the location 
#                 print('*'*50, request.user)
#                 car.seller = request.user
#                 car.location = location
#                 car.save()
#                 messages.info(request,'data saved :)')
#             else:
#                 raise Exception('Error')
#         except Exception as e:
#             print(e)
#             messages.error(request, f'an error happen {e}')
#     elif request.method == 'GET':
#         create_form = AddCarForm()
#         location_form = LocationForm()
#     return render(request, 'main/create_car.html', {
#         'create_form': create_form,
#         'location_form': location_form
#     })