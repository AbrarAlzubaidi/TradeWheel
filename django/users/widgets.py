from django.forms import widgets
from django.utils.safestring import mark_safe

class CustomImageField(widgets.FileInput): # why file input cause the image filed is a subset from the file field
    def render(self, name, value, attrs=None, **kwargs):
        old_image_html = super().render(name, value, attrs, **kwargs) # get the old html from the FileInput class
        new_image_html = ''
        if value and hasattr(value, 'url'): 
            new_image_html = mark_safe(f"<img src='{value.url}' width='200' class='mb-4'/>")  # value here it represent the image so to get the image we should access the url att 
        # we have to mark the new html inside the render function as safe html to make django accept it

        return f'{new_image_html}{old_image_html}'