# file is created by me 

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'rutu','place':'karad'}
    return render(request,'index.html',params)

#def removepun(request):
    '''
    #print (request.GET.get('text','default'))
    #get the text 
    djtext=request.GET.get('text','default')
    print(djtext)
    #analyze the text
    return HttpResponse("<strong>remove punck</strong> ")
    #return render(request,'index.html')
'''
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    count=request.POST.get('count','off')
    #print(removepunc)
    #print(djtext)
    #analyzed=djtext
    if(removepunc=='on'):
        punctuations='''!()-[];:'"\,<>./?@#$%^&*~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={"purpose":"remove punctuations", "analyzed_text":analyzed}
        #return HttpResponse(djtext)
        #return render(request,"analyze.html",params)
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={"purpose":"Changed to upper case", "analyzed_text":analyzed}
        #return HttpResponse(djtext)
        #return render(request,"analyze.html",params)
        djtext=analyzed
    if(newline=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        params={"purpose":"Newline text", "analyzed_text":analyzed}
        #return render(request,"analyze.html",params)
        djtext=analyzed
    if (count=="on"):
        analyzed=0
        for char in djtext:
                analyzed=analyzed+1
        params={"purpose":"Character count", "analyzed_text":analyzed}
        #return render(request,"analyze.html",params)
        djtext=analyzed

    return render(request,"analyze.html",params)

    
    

def exercise(request):
    s='''<a href='https://www.google.com' >1.Google</a> <br> 
        <a href='https://www.facebook.com'>2. Facebook</a>
        <br><a href ='https://youtube.com'>3.Youtube</a>
        '''


    return HttpResponse(s)

def about(request):
   # params={'name':'rutu','place':'karad'}
    return render(request,'about.html')









'''
def index(request):
    return HttpResponse('<h1>Hello Rutuja</h1>')

def about(request):
    return HttpResponse('About Hello Rutuja')

def services(request):
    return HttpResponse('About the services Hello Rutuja')

'''
'''
def index(request):
    return HttpResponse("home")

def removepun(request):
    return HttpResponse("remove punck ")
'''