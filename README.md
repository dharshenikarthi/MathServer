# Ex.05 Design a Website for Server Side Processing
## Date:26.11.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <title>Power Calculator</title>
</head>
<body>
    <h1>Power Calculator</h1>
    <form method="POST" action="">
        <label for="intensity">Intensity (I):</label>
        <input type="number" id="intensity" name="intensity" value="{{intensity}}"><br><br>
        <label for="resistance">Resistance (R):</label>
        <input type="number" id="resistance" name="resistance" value="{{resistance}}"><br><br>
        <input type="submit" value="Calculate Power" >
        <p id="result">{{Power}}</p>
    </form>
</body>
</html>


view.py

from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def power(request): 
    context={} 
    context['Power'] = "" 
    context['intensity'] = "" 
    context['resistance'] = "" 
    if request.method == 'POST': 
        print("POST method is used")
        i = request.POST.get('intensity','0')
        r = request.POST.get('resistance','0')
        print('request=',request) 
        print('Intensity=',i) 
        print('Resistance=',r) 
        power = int(i) ** 2 * int(r) 
        context['Power'] = "Power (P) = " + str(power) + " Watts" 
        context['intensity'] = i
        context['resistance'] = r 
        print('Power=',power) 
    return render(request,'mathapp/math.html',context)


urls.py

from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofbulb/',views.power,name="powerofbulb"),
    path('',views.power,name="powerofbulbroot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-11-26 210009.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-11-26 205843.png>)

## RESULT:
The program for performing server side processing is completed successfully.
