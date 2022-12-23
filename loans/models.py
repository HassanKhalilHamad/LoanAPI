from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=200)
    balance = models.IntegerField()

class Borrower(models.Model):
    name = models.CharField(max_length=200)

class Loan(models.Model):
    status = models.CharField(max_length=200)
    amount = models.IntegerField()
    period = models.IntegerField()
    BorrowerID = models.IntegerField(default=0)

class Offer(models.Model):
    LoanID = models.IntegerField()
    InvestorID = models.IntegerField()
    AIR = models.IntegerField()
    status = models.CharField(max_length=200)

class Payments(models.Model):
    LoanID = models.IntegerField()
    status = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateTimeField()