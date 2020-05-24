from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cocsite import forms
from datetime import datetime
from cocsite.models import Fund, Risk, Answer, Score, Answer_score, Result, Fund_Article, Fund_Article_Type, Stock_info
import time
import bs4,requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from gevent import monkey; monkey.patch_socket()
#import gevent
import csv
#import threading
# Create your views here.

@login_required(login_url = '/login/')
def homepage(request):
	stock_info = Stock_info.objects.all()
	articles = Fund_Article.objects.all()
	if request.method == 'POST':
		form_article = forms.fundarticle(request.POST)
		if form_article.is_valid():
			Article = form_article.cleaned_data['FundArticle']
		else:
			pass
		try:
			sc_type = Fund_Article_Type.objects.get(type_name=Article)
			scs = Fund_Article.objects.filter(article_type=sc_type.id)
		except:
			pass
	else:
		form_article = forms.fundarticle()
	return render(request,'index.html',locals())


def fund_article(request,ac_ty):
	articles = Fund_Article.objects.all()
	act = ac_ty
	return render(request,'fund_article.html',locals())

@login_required(login_url = '/login/')
def choice(request):
	fund_commodity = Fund.objects.all()
	if request.method == 'POST':
		form = forms.fundform(request.POST)
		if form.is_valid():
			fund_country = form.cleaned_data['fund_country']
			fund_risk = form.cleaned_data['fund_risk']
			fund_company = form.cleaned_data['fund_company']
		else:
			pass
		try:
			traget = Risk.objects.get(rank=fund_risk)
			selected_fund = Fund.objects.filter(rk=traget.id)
		except:
			pass
			
	else:
		form = forms.fundform()
	return render(request,'choice.html',locals())

@login_required(login_url = '/login/')	
def newplayer(request):
	return render(request,'newplayer.html',locals())

@login_required(login_url = '/login/')
def heart_test(request):
	ans_htmls = []
	ans1_targets = []
	value = 0
	answers = Answer.objects.all()
	answer_sc = Answer_score.objects.all()
	result = Result.objects.all()
	try:
		del_ans3s = Answer.objects.exclude(ans3='')
		del_ans4s = Answer.objects.exclude(ans4='')
	except:
		pass

	for i in answers:
		ans_htmls.append(request.POST.get(str(i)))
	
	try:
		for ans_html in ans_htmls:
			ans1_targets.append(Answer_score.objects.get(ans_sc=ans_html))
		for ans1_target in ans1_targets:
			value += int(str(ans1_target.score))
	except:
		pass
	
	if value >= 8 and value <= 14:
		value = 11
	elif value >= 15 and value <= 20:
		value = 17
	elif value >= 21 and value <= 26:
		value = 24
	elif value >= 27 and value <= 32:
		value = 30
	try:
		result_value = Result.objects.get(value=value)
	except:
		pass
	return render(request,'heart_test.html',locals())

@login_required(login_url = '/login/')
def oldplayer(request):
	return render(request,'oldplayer.html',locals())

def login(request):
	#post_form = forms.captchalogin(request.POST)
	user_all = User.objects.all()
	name = request.POST.get('username')
	password = request.POST.get('password')
	try:
		user = auth.authenticate(username=name, password=password) #使用者驗證
	except:
		user = None
	if user is not None:   #若驗證成功，以 auth.login(request,user) 登入
		if user.is_active:
			#if post_form.is_valid():
				auth.login(request,user) #登入成功
				return redirect('/') # 輸出到網頁上  #登入成功產生一個 Session，重導到<index.html>
				message = '登入成功!'
		else:
			message = '帳號尚未啟用!'
	else:
		message = '登入失敗!'
	return render(request,"login.html",locals())  #登入失敗則重導回<login.html>	

def logout(request):
    auth.logout(request)  #登出成功清除 Session，重導到<login.html>
    user_all = User.objects.all()
    name = request.POST.get('username')
    password = request.POST.get('password')
    return redirect('/')