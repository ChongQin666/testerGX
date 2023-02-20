from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from testerApp.models import Users
from testerApp.models import testItems
import json


def add_user(request):
    response = {}
    try:
        print("add_users success~")
        user = Users(id=request.GET.get('user_id'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def show_users(request):
    response = {}
    try:
        print("show_users success~")
        users = Users.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def show_testItems(request):
    response={}
    try:
        print("show_testItems success~")
        items=testItems.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", items))
        response['msg'] = 'success'
        response['error_num'] = 0

        print("*****************************************************************************")
        print(items)

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def add_testItems(request):
    response = {}
    try:
        temp = testItems(cpu=request.GET.get('cpu'))



        temp.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)













