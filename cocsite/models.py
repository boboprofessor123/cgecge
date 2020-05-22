from django.db import models

# Create your models here.

class Risk(models.Model):
	rank = models.CharField(max_length=10)

	def __str__(self):
 		return self.rank

class Fund(models.Model):
	rk = models.ForeignKey(Risk, on_delete=models.CASCADE)
	commodity = models.CharField(max_length=50)

	def __str__(self):
 		return self.commodity


class Question(models.Model):
	question = models.CharField(max_length=50)

	def __str__(self):
 		return self.question

class Answer(models.Model):
	ques = models.TextField(max_length=200)
	ans1 = models.CharField(max_length=50,blank=True)
	ans2 = models.CharField(max_length=50,blank=True)
	ans3 = models.CharField(max_length=50,blank=True)
	ans4 = models.CharField(max_length=50,blank=True)

	def __str__(self):
 		return self.ques
class Score(models.Model):
	sc = models.PositiveIntegerField(blank=True)
	sc_str = models.CharField(max_length=10)
	def __str__(self):
 		return self.sc_str

class Answer_score(models.Model):
	score = models.ForeignKey(Score, on_delete=models.CASCADE)
	ans_sc = models.CharField(max_length=50,blank=True)

	def __str__(self):
 		return self.ans_sc

class Result(models.Model):
	value = models.PositiveIntegerField(blank=True)
	category = models.CharField(max_length=10,blank=True)
	introduction = models.TextField(max_length=200,blank=True)

	def __str__(self):
 		return self.category

class Fund_Article_Type(models.Model):
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

class Fund_Article(models.Model):
	title = models.CharField(max_length=200,blank=True)
	source = models.CharField(max_length=50,blank=True)
	article_type = models.ForeignKey(Fund_Article_Type,on_delete=models.DO_NOTHING)
	date = models.CharField(max_length=20,blank=True)
	content = models.TextField(blank=True)
	def __str__(self):
		return self.title

class Stock_info(models.Model):
	title = models.CharField(max_length=20,blank=True,unique=True)
	price = models.CharField(max_length=20,blank=True,unique=True)
	increase = models.CharField(max_length=20,blank=True,unique=True)
	increase_pct = models.CharField(max_length=20,blank=True,unique=True)
	def __str__(self):
		return self.title


class Customer_info(models.Model):
	customer=models.CharField(max_length=200)
	birthday=models.CharField(max_length=20)
	income=models.PositiveIntegerField(default=0)
	career=models.CharField(max_length=20)
	gender= models.PositiveIntegerField(default=0)
	is_app_bank=models.PositiveIntegerField(default=0)
	marital=models.CharField(max_length=20)
	dependents=models.PositiveIntegerField(default=0)
	residence=models.CharField(max_length=20)
	is_register_web_bank=models.PositiveIntegerField(default=0)
	is_register_mobile_pay=models.PositiveIntegerField(default=0)
	credit_level=models.CharField(max_length=20)
	period= models.PositiveIntegerField(default=0)
	balance_loan= models.PositiveIntegerField(default=0)
	usage=models.CharField(max_length=20)
	property_house=models.CharField(max_length=20)
	percent= models.PositiveIntegerField(default=0)
	situation=models.CharField(max_length=20)
	insurance_category=models.CharField(max_length=20)
	insurance_premiums= models.PositiveIntegerField(default=0)
	is_active= models.PositiveIntegerField(default=0)
	is_blacklist= models.PositiveIntegerField(default=0)
	claim_amount= models.PositiveIntegerField(default=0)
	claim_descript=models.CharField(max_length=20)
	dividend_category=models.CharField(max_length=20)
	fund_name=models.CharField(max_length=20)
	price_currency=models.CharField(max_length=20)
	net= models.PositiveIntegerField(default=0)