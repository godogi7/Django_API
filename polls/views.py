from .models import *
# index.html 파일을 렌더링해주는 라이브러리
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
#from django.http import Http404

def index(request):
    # Question 모델에서 가장 최근에 생성된 5개의 질문을 내림차순으로 가져오려고
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    #context = {'first_question': latest_question_list[0]}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    # value="{{ choice.id }} 의 값들이 들어감 
    # 에러 처리
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        # 두개의 서버에서 동시에 update 요청해도 잘 작동 함
        selected_choice.votes  = F('votes') +1
        selected_choice.save()
        return  HttpResponseRedirect(reverse('polls:result', args = (question_id, )))
        # 사용자를 다른 페이지로 이동시킴
        # result는 question_id 줘야함
        # ( 무조건 ,(컴마) 넣어줘야 함 = 여러개의 argument 들어갈 수 있는데 그 중에 하나로 퀘스텬 아이디 들어간단 소리)
        


def result(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html', {'question': question})