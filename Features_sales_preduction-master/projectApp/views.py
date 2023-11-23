from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import joblib
import itertools
# Create your views here.
def index(request):
  ans=Predict.objects.order_by('-id')[0:1]
  if request.method == 'POST':
    form = Features_sales_preductionForm(request.POST)
    model = joblib.load('Features_scale_preduction.sav')
    lst = []
    if form.is_valid():
      TV = form.cleaned_data['TV']
      Radio = form.cleaned_data['Radio']
      Newspaper = form.cleaned_data['Newspaper']
      a = Features_sales_preduction(TV=TV, Radio=Radio, Newspaper=Newspaper)
      a.save()
      lst.append(TV)
      lst.append(Radio)
      lst.append(Newspaper)
      print(lst)
      lst = [float(i) for i in lst]
      ans = model.predict([lst])
      # listToStr = ' '.join([str(elem) for elem in cls])
      ans = [ y for x in ans for y in x]
      print(ans)
      ans = Predict(Predict=ans).save()
      return redirect('index')
  else:
      form = Features_sales_preductionForm()    
  return render(request, "Html_page/index.html",{'form':form,'ans':ans})
