from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from monitor.models import Question
from django.template import RequestContext, loader
from .forms import AddForm


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'detail.html', {'question': question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
def form(request):
	if request.method == 'POST':# 当提交表单时
	 
		form = AddForm(request.POST) # form 包含提交的数据
		 
		if form.is_valid():# 如果提交的数据合法
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			return HttpResponse(str(int(a) + int(b)))
	 
	else:# 当正常访问时
		form = AddForm()
	return render(request, 'form.html', {'form': form})
def home(request):
	return render(request, 'home.html')
