from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def power(request): 
    context={} 
    context['Power'] = "" 
    context['intensity'] = "0" 
    context['resistance'] = "0" 
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

