from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

taxrate = 0.15
def empty(request):
    return HttpResponse('this is a site to calculate tax')
    # I don't know Whether you Required an HTTPresponse or 
    # to render an HTML file so I did both you can remove the hashtag to make it return an HTML file
    #return render(request,"/Users/hemoo/Desktop/IS424/lab4/l4project/app/templates/empty.html")

def calc(request,num):
    price =float(num)*taxrate
    return render(request,"/Users/hemoo/Desktop/IS424/lab4/l4project/app/templates/calc.html",
                  {'price':price , 'num':num , 'total':float(num)+price})
def tax(request):
    return render(request ,"/Users/hemoo/Desktop/IS424/lab4/l4project/app/templates/tax.html" , {'taxrate':taxrate*100})
# for Some reason I couldn't write the short path of the HTML files without having "Template doesn't exist error ""
# so I had to use the full Path