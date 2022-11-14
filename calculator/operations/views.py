
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from functools import reduce
class Additionview(APIView):
    def post(self,request,args,*kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response(data=res)
class Subview(APIView):
    def post(self,request,args,*kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response(data=res)
class Factview(APIView):
    def post(self,request,args,*kwargs):
        n=request.data.get("num")
        fact=1
        for i in range (1,(n+1)):
            fact=fact*i
        return Response(data=fact)
class Primeview(APIView):
    def post(self,request,args,*kwargs):
        n=request.data.get("num")
        is_prime=True
        for i in range(2,n):
            if(n%i==0):
                is_prime=False
                break
        return Response(data=is_prime)
class Maxnumview(APIView):
    def post(self,request,args,*kwargs):
        print(request.data)
        lst=request.data.get("numbers")
        lst.sort(reverse=True)
        print(lst)
        mlist=reduce(lambda n1,n2:(n1+n2) if int(n1+n2)>int(n2+n1) else (n2+n1),lst)
        return Response(data=mlist)