from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm
from causes.models import Causes
from news.models import News

def homePage(request):
    causesData = Causes.objects.all().order_by('-title')[0:3]
    data={
        'title':'New Home Page',
        'bdata':'I am learning django',
        'clist':['PHP','Java','Django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'karamjeet', 'age':21},
            {'name':'deepak','age':34}
        ],
        'causesData':causesData
    }
    return render(request, "index.html", data)
    # return HttpResponse('Welcome to django project')

def aboutUs(request):
    output = ''
    if request.method=='GET':
        output = request.GET.get('output')
    return render(request, "news.html",{'output':output})
    # return HttpResponse('Welcome to django project',{'output':output})

def course(request):
    return HttpResponse('Welcome to course page')

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def news(request):
    newsData = News.objects.all()
    data={
        'newsData':newsData
    }
    return render(request, "news.html", data)

def donate(request):
    return render(request, "donate.html")

def userform(request):
    output=0
    data={}
    uf=usersForm()
    data={'form':uf}
    try:
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            output = n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':output
            }
            url = "/about-us/?output={}".format(output)
            return redirect(url)
    except:
        pass
    return render(request, "userform.html",data)

def submitform(request):
    try:
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            output = n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':output
            }
            print('data',data)
            url = "/about-us/?output={}".format(output)
            return redirect(url)
    except:
        pass

def evenorodd(request):
    try:
        result =''
        if request.method=='POST':
            number = int(request.POST.get('number'))
            if number%2==0:
                result = 'Even Number'
            else:
                result = 'Odd Number'
    except:
        pass
    return render(request, "evenorodd.html", {'result':result})

def marksheet(request):
    try:
        if request.method=='POST':
            subject1 = eval(request.POST.get('subject1'))
            subject2 = eval(request.POST.get('subject2'))
            subject3 = eval(request.POST.get('subject3'))
            subject4 = eval(request.POST.get('subject4'))
            subject5 = eval(request.POST.get('subject5'))
            total = subject1+subject2+subject3+subject4+subject5
            percentage = total/5
            return render(request, "marksheet.html", {'total':total,'percentage':percentage})
    except:
        pass
    return render(request, "marksheet.html")