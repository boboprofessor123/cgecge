from django.contrib import admin
from cocsite.models import Fund, Risk, Answer, Score, Answer_score, Result,Fund_Article_Type,Fund_Article, Stock_info,Customer_info
# Register your models here.

admin.site.register(Fund)
admin.site.register(Risk)
admin.site.register(Answer)
admin.site.register(Score)
admin.site.register(Answer_score)
admin.site.register(Result)
admin.site.register(Fund_Article_Type)
admin.site.register(Stock_info)
admin.site.register(Fund_Article)
admin.site.register(Customer_info)