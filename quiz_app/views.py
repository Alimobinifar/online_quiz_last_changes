from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from random import randint
from .models import Questions ,Cat , Answers,Exsam
from django.db.models import Count
# from django.db.models import Coun
from random import sample


def show_questions(request,id):
    if request.method=="GET":
        try:
            return JsonResponse({"data":Exsam.objects.get(exsam_id=id).soalat})
        except:
            query_set=list(Cat.objects.all())

            result={}
            for data in query_set:
                rand=sample(list(data.question.all()),1)
                for qs in  rand:
                    ans = qs.answer.all()
                    result[qs.id]={qs.title:{}}
                    count = 0
                    for javab in  ans :
                        count+=1
                        result[qs.id][qs.title][count]=javab.title
                    
            Exsam.objects.create(soalat=result,exsam_id=id)
            return JsonResponse({'data':result})
        else:
            return JsonResponse({"status": "error"})    


@csrf_exempt
def show_result(request,id):

    if request.method=="POST":
        javab_user = json.loads(request.body.decode("utf-8"))
        score = 0
        soalat_exsam = Exsam.objects.get(exsam_id=id).soalat
        for elm in soalat_exsam:
            print(elm)
            javab = Questions.objects.get(id=elm).answer.filter(is_correct=True)
            print(javab[0],javab_user[elm])
            if javab[0]==soalat_exsam[elm][javab_user[elm]]:
                score+=1
            else :
                score-=0.5
    return JsonResponse({"score":score})



    
