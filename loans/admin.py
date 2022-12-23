from django.contrib import admin
from .models import *

admin.site.register([Investor,Borrower,Loan,Offer,Payments])