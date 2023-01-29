def upload_image(instance, filename):
    path = f'profile_image/user_{instance.user.id}/{filename}'
    return path