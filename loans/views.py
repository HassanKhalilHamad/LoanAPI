from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from apscheduler.schedulers.background import BackgroundScheduler
from .PaymentLogic import *
from datetime import datetime, timedelta

sched = BackgroundScheduler()
sched.add_jobstore('sqlalchemy', url='sqlite:///jobstores.db')
sched.start()

@api_view(['POST'])
def Loan_request(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def Offer_Submit(request):
    serializer = OfferSerializer(data=request.data)
    investor = Investor.objects.get(pk=request.data["InvestorID"])
    loan = Loan.objects.get(pk=request.data["LoanID"])
    if serializer.is_valid() and investor.balance > loan.amount+3:
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({"Status":"NO Balance"},status=status.HTTP_200_OK)

@api_view(['GET'])
def View_Offers(request):
    offer = Offer.objects.get(status="Pending")
    serializer = OfferSerializer(offer)
    return JsonResponse({"Data":serializer.data})

@api_view(['POST'])
def Accept_Offer(request):
    offer = Offer.objects.get(pk=request.data["OfferID"])
    loan = Loan.objects.get(pk=offer.LoanID)
    investor = Investor.objects.get(pk=offer.InvestorID)
    if investor.balance > loan.amount + 3:
        offer.status = "Accepted"
        offer.save()
        loan.status="Funded"
        loan.save()

        prmonth,period = PaymentLogic.payment_plan(offer,loan)
        next_time = 30
        for i in range(period):
            _date = datetime.now() + timedelta(seconds=next_time)
            next_time+=30
            sched.add_job(PaymentLogic.creat_payment, 'date', run_date=_date, args=[prmonth,loan])
        return JsonResponse({"Status":"Offer accepted"},status=status.HTTP_200_OK)
    else:
        return JsonResponse({"Status":"Offer Not accepted","Reson":"Investor Balance is low"},status=status.HTTP_200_OK)


@api_view(['POST'])
def Make_Payment(request):
    paymentID = request.data["paymentID"]
    payment = Payments.objects.get(pk=paymentID)
    payment.status = "Paid"
    payment.save()
    loan = Loan.objects.get(pk = payment.LoanID)
    if PaymentLogic.check_payments(loan):
        loan.status  = "Completed"
        loan.save()
    return JsonResponse({"Status":"Payment Confirmed"},status=status.HTTP_200_OK)