from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Car
from users.models import Profile
from .forms import AddCarForm
from users.forms import LocationForm
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
    return render(request, "main/home.html", {
        "car_list":car_list,
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