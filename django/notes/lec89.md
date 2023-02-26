# django async operation by jquery

for like/dislike process we prepare the relation between the car and the profile, view and url. and we test it via browser/admin panel and it works

now we need just to add this logic in the user interface via jquery

[jquery](https://releases.jquery.com/)

```js
$.ajax({
    type: "POST", // type of the request
    url: "{% url 'like' car_id=listing.id %}", // target view url here its the like view
    data: {
        'csrfmiddlewaretoken': "{{ csrf_token }}" // pass the token to avoid the forbidden error
    },
    dataType: "json", // the datatype of the data that passed above
    success: function(r){ // success function will execute when the ajax request done successfuly
        alert('added')
    },
    error: function(r){ // error function will execute when an error acurred with the ajax request 
        alert('error')
    }
})
```