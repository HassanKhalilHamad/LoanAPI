from datetime import datetime
from .models import *
from .serializers import *


class PaymentLogic():

    

    def payment_plan(offer,loan):
        totalamount = (loan.amount * (offer.AIR / 100)) + loan.amount
        perMonth = totalamount // loan.period
        return perMonth , loan.period

    def creat_payment(amount,loan):
        payment = Payments()
        payment.LoanID = loan.pk
        payment.amount = amount
        payment.status = "Not Paid"
        payment.date = datetime.now()
        payment.save()

    def check_payments(loan):
        allPayments = Payments.objects.filter(LoanID=loan.pk).filter(status="Paid")
        if len(allPayments) == loan.period:
            return True
        else:
            return False
