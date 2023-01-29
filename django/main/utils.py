def upload_image(instance, filename):
    path = f'profile_image/user_{instance.seller.user.id}/car_images/car_{instance.id}/{filename}'
    return path