from django.shortcuts import render, redirect
from .models import Station_search
from .forms import SearchForm
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'main_app/index.html')


def createform(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = SearchForm(request.POST, request.FILES)

        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('/main_app/result')

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = SearchForm()

    return render(request, 'main_app/form_create.html', {'form': form})

def result(request):
    return render(request, 'main_app/result.html')



'''
def main_page(request): #index
    return render(request,'index/index.html')
'''
'''
def result_page(request, words):
    typed_words = Station_search.objects.get(id=question_id)
    if request.method == "POST" :
        text = request.POST['text']
        return render(request,'main_app/result_page.html')
'''