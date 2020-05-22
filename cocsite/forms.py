from django import forms
from captcha.fields import CaptchaField

class fundform(forms.Form):
	COUNTRY = [
		['國內/境外','國內/境外'],
		['國內','國內'],
		['國外','國外'],
	]
	RISK = [
		['風險屬性','風險屬性'],
		['保守型','保守型'],
		['積極型','積極型'],
		['穩健型','穩健型'],
		['成長型','成長型'],
	]
	COMPANY = [
		['計價幣別','計價幣別'],
		['USD','USD'],
		['NTD','NTD'],
		['RMB','RMB'],
	]

	fund_country = forms.ChoiceField(label='國內境外', choices=COUNTRY)
	fund_risk = forms.ChoiceField(label='風險屬性', choices=RISK)
	fund_company = forms.ChoiceField(label='計價幣別', choices=COMPANY)

class fundarticle(forms.Form):
	Article = [
		['最新消息','最新消息'],
		['境外、股票型','境外、股票型'],
		['台股、陸股、大中華','台股、陸股、大中華'],
		['能源、黃金貴金屬','能源、黃金貴金屬'],
		['REIT、ETF、平衡型','REIT、ETF、平衡型'],
		['生技農業、特殊資源','生技農業、特殊資源'],
		['債券、貨幣型','債券、貨幣型'],
		['綜合分析','綜合分析'],
	]
	
	FundArticle = forms.ChoiceField(label='最新消息', choices=Article)


class captchalogin(forms.Form):
	captcha = CaptchaField()

