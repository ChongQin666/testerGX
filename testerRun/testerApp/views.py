from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from testerApp.models import Users, SNTestLog
from testerApp.models import TestItems
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
    testItemForJson=TestItems()
    try:
        print("show_testItems success~")
        items = TestItems.objects.filter()
        # items=testItems.objects.filter().values()
        # for eachItem in items:
        #     if eachItem['cpu']==True:
        #         testItemForJson.cpu=True
        #     else:
        #         testItemForJson.cpu = False
        #     if eachItem['mem']==True:
        #         testItemForJson.mem=True
        #     else:
        #         testItemForJson.mem = False
        #     if eachItem['fan']==True:
        #         testItemForJson.fan=True
        #     else:
        #         testItemForJson.fan = False
        #     if eachItem['hdd']==True:
        #         testItemForJson.hdd=True
        #     else:
        #         testItemForJson.hdd = False
        #     if eachItem['pcie']==True:
        #         testItemForJson.pcie=True
        #     else:
        #         testItemForJson.pcie = False
        #     if eachItem['bios']==True:
        #         testItemForJson.bios=True
        #     else:
        #         testItemForJson.bios = False
        #     if eachItem['fru']==True:
        #         testItemForJson.fru=True
        #     else:
        #         testItemForJson.fru = False
        #     if eachItem['sdd']==True:
        #         testItemForJson.sdd=True
        #     else:
        #         testItemForJson.sdd = False
        #     if eachItem['usb']==True:
        #         testItemForJson.usb=True
        #     else:
        #         testItemForJson.usb = False
        #     if eachItem['id_light']==True:
        #         testItemForJson.id_light=True
        #     else:
        #         testItemForJson.id_light = False
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
        temp = TestItems(cpu=request.GET.get('cpu'))



        temp.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def sn_scan_info(request):
    response={}
    # snTestLog=SNTestLog()
    try:
        print("show SN scan Info success~")

        # snTestLog=SNTestLog(sn=request.GET.get("sn"))
        sn = request.GET.get("sn")

        snTestLog = SNTestLog.objects.filter(SN=sn)

        testItems=TestItems.objects.filter(SN=sn).values()
        #查询集展开并设置为json数据
        testItems_data=[]
        for i in testItems:
            testItems_data.append(i)

        print(json.dumps(testItems_data[0]))

        response['list1'] = json.loads(serializers.serialize("json", snTestLog))

        # response['list2'] = json.loads(serializers.serialize("json", testItems_data))
        response['list2'] = json.dumps(testItems_data)

        response['msg'] = 'success'
        response['error_num'] = 0

        print("*****************************************************************************")
        print(snTestLog)

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)









