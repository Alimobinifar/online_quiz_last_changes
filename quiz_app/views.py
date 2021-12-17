from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from random import randint
from .models import Questions ,Cat , Answers
# from django.db.models import Coun


def show_questions(request):
    if request.method=="GET":
        query_set=list(Cat.objects.all())
        # query_set2=list(Questions.objects.filter(cat=''))
        result=[]
        for data in query_set:
            for qs in data.question.all():
                    result.append(qs.title)

        return JsonResponse({'data':result})
        
    else:
        return JsonResponse({"status": "error"})    










    # if request.method == "GET":
    #     query_set =list(Cat.objects.filter(cat='Geography'))
    #     result = []
    #     for data in query_set:
    #         for qs in data.question.all():
    #             result.append(qs.title)
    #     return JsonResponse({'data':result})
    # else:
    #     return JsonResponse({"status": "error", "msg": "faghat get mojazeh"}, status=403)
    


    
