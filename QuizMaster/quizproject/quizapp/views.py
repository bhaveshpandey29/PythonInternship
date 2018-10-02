from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Quiz
# Create your views here.

def index(request):
    quizapp = Quiz.objects.all()[:10]

    context = {
        'quizapp' : quizapp
    }
    return render(request,'index.html',context)

def details(request,id):
    qz = Quiz.objects.get(id = id)
    context = {
        'qz' : qz
    }
    return render(request,'details.html',context)

def result(request,result,id):
    if(request.method == 'POST'):
        qz = Quiz.objects.get(id = id)
        context = {
            'qz' : qz
        }  
        return render(request,'result.html',context)
    else:
        pass

def add(request):
    if(request.method == 'POST'):
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']  
        answer = request.POST['answer']      

        quiz = Quiz(question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
        quiz.save()
        return redirect('/start')
    else:
        return render(request,'add.html')