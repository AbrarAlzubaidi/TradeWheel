# learn-django 
*instructor: Hussain Mustafa*
*languages that cover in the course: HTML, CSS, Bootstrap, Javascript, jQuery, Python 3, and Django!*


**notes i will add it to review it whenever i need it**

1. what is django?
    > django is python based framework to build a web applications (Backend side)

2. type of websites that live in the internet?
- static websites dont interact taht much with the user (all user will see the same site content) like: resume websites, portfolio websites, brochure websites, one-off landing pages, and other informational or read-only sites.
- dynamic websites: that interact with the user (each user will see different site content), which have a server side (what was cooked hidden from the user, database that will store his/her information, user cant interact with) and client side (client side represent the interface that user interact with, and it maybe a one page or multi pages) 

| client side | server side|
|-------------|------------|
|does't need interaction with the server|needs interactions with the server|
|run's on user computer|run's on the web server|
|reduces load on the server's proccessing unit|allow the server to provide dynamic websites tailored to the user increases the proccessing load on server|
|languages: HTML, CSS, vanilla JS or its libraries|languages: PHP, ASP.net, Python, NodeJs|

3. why django?
- ridiculously fast, quick prototyping and app development
- secure, security is baked into the framework
- scalable, quickly and flexibly change scale
- reusability, application logic divided into smaller apps
- community, huge developer community                      

4. django features:
- MVT: model, view, template design pattern
- build in powerfull ORM (object-relational mapping)
- middleware: CSRF protection, caching, authentication, ...
- flexible templating language
- server side 
- excellent documentation
- build-in form handling


5. browser have many differntiate parts, the 2 most important of them in theis course is:
- the rendering engine (that transform HTML and CSS)
- the JS interpreter (that execute the JS files)

6. how to add a jquery in html?
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
```

7. example of jquery
```js
$("p").remove(); // select all the p tags and remove them
```
8. when python invented by? 

    Guid van rossum

9. where we use python?
   - web development
   - data analysis
   - software development
   - system scraping
   - artifical intelligent
   - machine learning
   - mathmatics
   - internt of things
   - game development

10. what are python features?
    - interpreter language: execute each line of code sequentially (line by line)
    - dynamacillay typed language: means that we dont have to specifiy the datatype of a variable
    - portable
    - high level programing language
    - automic memory managment
    - interactive shell
    - basic types: numbers, strings
    - container types: lists, dictionaries, tuples
    - variables
    - control structure
    - functions and procedures
    - classes and instances
    - modules and packages
    - exceptions
    - files and standard library

11. variables in django: an important example
```python
x = "i am a global variable"
def fun():
    global x 
    x = "now i changed by function"
print(x) # i am a global variable
fun()
print(x) # now i changed by function
# if you didnot add global keyword it will not changed
```

12. tuples:
```python
t = (1,2,3,4,2)
print(t) # 1,2,3,4,2
print(t[1]) #2
t[1] = 80 # Error cant change tuple elements value
```

13. sets:
```python
s = {1,2,3,4,2} # it drops the duplicated value
print(s) # 1,2,3,4
print(s[1]) #2
s[1] = 80 # Error cant change set elements value
```

14. inheretance in classes:
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name) # we can do it in different way Person.__init__(name)
        self.grade = grade
```

15. what is middleware?
> Middleware is software that provides common services and capabilities to applications outside of what’s offered by the operating system.

Middleware helps developers build applications more efficiently. It acts like the connective tissue between applications, data, and users.

Middleware we make it like before we accsess the backend for authentacation for example so if the middleware didnot accept the username and password (if we imagine that the user didnot enter the password correctly) so the middleware will send an error mesg so the request will not continue to the backend to get the error response, the response will send from the middleware not from the backend 

so we consider that the middleware is like a check point before we acheave the backend.


and there are types of middleware:
- build in middleware
- auth middleware
- error handler middleware
- database middleware
- etc...

from [redhat middleware](https://www.redhat.com/en/topics/middleware/what-is-middleware)



### course resources:
- [django docs](https://docs.djangoproject.com/en/4.1/)
- [python offical site](https://www.python.org/)
- [preneure](https://preneure.com/)
