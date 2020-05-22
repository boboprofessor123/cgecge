from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cocsite import forms
from datetime import datetime
import bs4,requests
from cocsite.models import Fund, Risk, Answer, Score, Answer_score, Result, Fund_Article, Fund_Article_Type, Stock_info
from captcha.fields import CaptchaField
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading
# Create your views here.


@login_required(login_url = '/login/')
def homepage(request):

	def web_bug():
		#lock.acquire()
		chrome_options = Options() # 啟動無頭模式
		chrome_options.add_argument('--headless')  #規避google bug
		chrome_options.add_argument('--disable-gpu')
		driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
		driver.get('https://tw.stock.yahoo.com/us/worldidx.php')
		#driver = requests.get('https://tw.stock.yahoo.com/us/worldidx.php').text
		soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
		stock = soup.select("body > center > table:nth-child(11) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > a")
		number = soup.select("#trade > b")
		up_down = soup.select("body > center > table:nth-child(11) > tbody > tr > td > table > tbody > tr > td:nth-child(4)")
		up_down_percent = soup.select("body > center > table:nth-child(11) > tbody > tr > td > table > tbody > tr > td:nth-child(5)")
		stock_num = [stock[1].text, stock[2].text, stock[8].text, stock[14].text, stock[15].text]
		number_num = [number[0].text, number[1].text, number[7].text, number[12].text, number[13].text]
		updown_num = [up_down[1].text, up_down[2].text, up_down[8].text, up_down[14].text, up_down[15].text]
		updown_pct_num = [up_down_percent[1].text, up_down_percent[2].text, up_down_percent[8].text, up_down_percent[14].text, up_down_percent[15].text]
		stock_info = Stock_info.objects.all()
		stock_info.delete()
		for sn,nn,un,upn in zip(stock_num,number_num,updown_num,updown_pct_num):
			st_inf = [sn,nn,un,upn]
			sf = Stock_info.objects.create(title=st_inf[0], price=st_inf[1], increase=st_inf[2], increase_pct=st_inf[3])
			sf.save()
		driver.quit()
		#lock.release()
	def req_bug():
		new_links = list()
		all_new_links = list()
		arc_area_del = ['富達基金情報','投資風向球']
		#lock.acquire()
		driver2 = requests.get('https://fund.udn.com/fund/cate/5853').text
		soup2 = bs4.BeautifulSoup(driver2, 'html.parser')
		news = soup2.find_all('dt', 'big')
		arc_area = soup2.find_all('div', 'area category_box')
		for new in news:
			new_links.append(new.find('a')['href']) #文章的網址
		for new_link in new_links:
			driver_new = requests.get(new_link).text
			soup_new = bs4.BeautifulSoup(driver_new, 'html.parser')
			arc_area = soup_new.find(id='nav').find('b').text
			if arc_area not in arc_area_del:
				arc_title = soup_new.find(id='story_art_title').text #文章標題
				arc = soup_new.find(id='story_body_content')
				arc_texts = arc.find_all('p') #文章內容
				arc_date = soup_new.find('div', 'shareBar__info--author').find('span').text #文章日期
				arc_source = soup_new.find('div', 'shareBar__info--author').text #文章日期
				articles = Fund_Article.objects.all()
				#article_ty = Fund_Article_Type.objects.all()
				articles.delete()
				ac_ty = Fund_Article_Type.objects.get(type_name='最新消息')
				print(ac_ty)
				arc_model = Fund_Article.objects.create(title=arc_title,source=arc_source,article_type=ac_ty,date=arc_date,content=arc_texts)
				arc_model.save()			
			else:
				pass
		all_news = soup2.find_all('dt', 'more1_5853')
		for all_new in all_news:
			all_new_links.append(all_new.find('a')['href']) #文章的網址
		for all_new_link in all_new_links:
			driver_all = requests.get(all_new_link).text
			soup_all = bs4.BeautifulSoup(driver_all, 'html.parser')
			all_arc_area = soup_all.find(id='nav').find('b').text
			if all_arc_area not in arc_area_del:
				all_arc_title = soup_all.find(id='story_art_title').text #文章標題
				all_arc = soup_all.find(id='story_body_content')
				all_arc_texts = arc.find_all('p') #文章內容
				all_arc_date = soup_all.find('div', 'shareBar__info--author').find('span').text #文章日期
				all_arc_source = soup_all.find('div', 'shareBar__info--author').text #文章日期
				all_ac_ty = Fund_Article_Type.objects.get(type_name=all_arc_area)
				print(all_ac_ty)
				all_arc_model = Fund_Article.objects.create(title=all_arc_title,source=all_arc_source,article_type=all_ac_ty,date=all_arc_date,content=all_arc_texts)
				all_arc_model.save()
			else:
				pass
			#lock.release()
	#lock=threading.Lock()
	rq_bg = threading.Thread(target=req_bug)
	wb_bg = threading.Thread(target=web_bug)
	#web_bug()
	#rq_bg.start()
	req_bug()
	wb_bg.start()
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

