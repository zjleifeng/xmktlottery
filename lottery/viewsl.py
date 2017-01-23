#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 14:41
# @Author  : eric
# @Site    :
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render,render_to_response

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from lottery.forms import UpForm
from xmktlottery import settings
import os
import xlrd
from time import strftime,localtime
from django.shortcuts import render,render_to_response
from django.template import RequestContext
import random
from django.views.decorators.csrf import csrf_exempt
import json
from lottery.models import Person,Result
from django.db.models import Q

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def lot5(request):

    res_num = Result.objects.filter(awardname='五等奖',isdel=0).count()
    if res_num < 16:
        if res_num == 0:
            toolot = '五等奖第一轮'
            res_num=True
        elif res_num < 6:
            toolot = '五等奖第二轮'
        elif res_num < 11:
            toolot = '五等奖第三轮'
        else:
            toolot = '五等奖第四轮'


        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot5.html', {
                'userlist': json.dumps(user_list),
                'toolot':toolot,
                'res_num': res_num
        })
    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False,
            'res_num': None
        })

@login_required
def update5(request):
    res_num = Result.objects.filter(awardname='五等奖',isdel=0).count()
    if res_num < 16:
        obj_list = Person.objects.filter(isWin=0)


        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 5)




        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='五等奖')

        toolnum=Result.objects.filter(awardname='五等奖',isdel=0).count()

        win_list.append({"toolnum":toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False

        })

@login_required
def cho5(request):
    chonum=Result.objects.filter(awardname='五等奖',isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot4(request):
    res_num = Result.objects.filter(awardname='四等奖',isdel=0).count()
    if res_num < 6:
        if res_num == 0:
            toolot = '四等奖第一轮'

        elif res_num ==3:
            toolot = '四等奖第二轮'

        else:
            toolot = '四等奖第三轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot4.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum':res_num
        })
    else:
        return render(request, 'lots/lot4.html', {
            'toolot': False

        })

@login_required
def update4(request):
    res_num = Result.objects.filter(awardname='四等奖',isdel=0).count()
    if res_num < 6:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})
        if res_num==0:

            win_list = random.sample(user_list, 3)
        elif res_num==3:
            win_list = random.sample(user_list, 2)


        else:
            win_list = random.sample(user_list, 1)
        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='四等奖')
        toolnum = Result.objects.filter(awardname='四等奖',isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return HttpResponse("错误操作！")

@login_required
def cho4(request):
    chonum=Result.objects.filter(awardname='四等奖',isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot3(request):
    res_num = Result.objects.filter(awardname='三等奖',isdel=0).count()
    if res_num < 3:
        if res_num == 0:
            toolot = '三等奖第一轮'
        else:
            toolot = '三等奖第二轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot3.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot3.html', {
            'toolot':False

        })

@login_required
def update3(request):
    res_num = Result.objects.filter(awardname='三等奖',isdel=0).count()
    if res_num < 3:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})
        if res_num == 0:

            win_list = random.sample(user_list, 2)

        else:
            win_list = random.sample(user_list, 1)
        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='三等奖')
        toolnum = Result.objects.filter(awardname='三等奖',isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return HttpResponse("错误操作！")

@login_required
def cho3(request):
    chonum = Result.objects.filter(awardname='三等奖',isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot2(request):
    res_num = Result.objects.filter(awardname='二等奖',isdel=0).count()
    if res_num <2:
        if res_num == 0:
            toolot = '二等奖第一轮'
        else:
            toolot = '二等奖第二轮'

        return render(request, 'lots/lot2.html', {
            'toolot': toolot

        })

    else:
        return render(request, 'lots/lot2.html', {
            'toolot': False

        })

@login_required
def update2(request):
    res_num = Result.objects.filter(awardname='二等奖',isdel=0).count()
    obj_list = Person.objects.filter(isWin=0)

    if res_num < 2:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})


        win_list = random.sample(user_list, 1)


        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='二等奖')
        toolnum = Result.objects.filter(awardname='二等奖',isdel=0).count()
        if toolnum==1:

            win_list.append({"toolnum": True})
        else:
            win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot2.html', {
            'toolot': False

        })

@login_required
def cho2(request):
    chonum=Result.objects.filter(awardname='二等奖',isdel=0).count()

    return HttpResponse(chonum)

@login_required
def lot1(request):
    res_num = Result.objects.filter(awardname='一等奖',isdel=0).count()

    if res_num == 0:
        toolot = '一等奖'
        return render(request, 'lots/lot1.html', {
                'toolot': toolot

            })
    else:
        return render(request, 'lots/lot1.html', {
            'toolot': False

        })

def update1(request):
    res_num = Result.objects.filter(awardname='一等奖',isdel=0).count()
    obj_list = Person.objects.filter(isWin=0)
    if res_num == 0:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='一等奖')
        #toolnum = Result.objects.filter(awardname='二等奖').count()

        win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot1.html', {
            'toolot': False

        })

@login_required
def cho1(request):
    chonum=Result.objects.filter(awardname='一等奖',isdel=0).count()

    return HttpResponse(chonum)

@login_required
def lott(request):
        res_num = Result.objects.filter(awardname='特等奖',isdel=0).count()

        if res_num == 0:
            toolot = '特等奖'
            return render(request, 'lots/lott.html', {
                'toolot': toolot

            })
        else:
            return render(request, 'lots/lott.html', {
                'toolot': False

            })

@login_required
def updatet(request):
        res_num = Result.objects.filter(awardname='特等奖',isdel=0).count()
        obj_list = Person.objects.filter(isWin=0)
        if res_num == 0:
            user_list = []
            for user_obj in obj_list:
                tel = user_obj.tel
                num = user_obj.num
                user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

            win_list = random.sample(user_list, 1)

            for win in win_list:
                uid = win.get('id')
                p = Person.objects.get(id=uid)
                Person.objects.filter(id=uid).update(isWin=1)
                Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='特等奖')
            # toolnum = Result.objects.filter(awardname='二等奖').count()

            win_list.append({"toolnum": False})
            return HttpResponse(json.dumps(win_list), content_type="application/json")
        else:
            # HttpResponse(json.dumps(win_list), content_type="application/json")
            return render(request, 'lots/lott.html', {
                'toolot': False

            })

@login_required
def chot(request):
    chonum=Result.objects.filter(awardname='特等奖',isdel=0).count()

    return HttpResponse(chonum)

@login_required
def lotj2(request):

    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})
    toolot = '加奖'
    return render(request, 'lots/lotj2.html', {
        'userlist': json.dumps(user_list),
        'toolot': toolot,
    })

@login_required
def updatej2(request):
    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        name=user_obj.name
        l=name
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 1)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    # toolnum = Result.objects.filter(awardname='二等奖').count()

    #win_list.append({"toolnum": False})
    return HttpResponse(json.dumps(win_list), content_type="application/json")



@login_required
def lotj1(request):

    toolot = '加奖'
    return render(request, 'lots/lotj1.html', {
            'toolot': toolot

        })


@login_required
def updatej1(request):

        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
        # toolnum = Result.objects.filter(awardname='二等奖').count()

        #win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")






#继续抽奖（中奖不重复）
@login_required
@csrf_exempt
def dellottyers(request):
    request.session['where_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method=='POST':
        Result.objects.all().update(isdel=1)
    else:
        return HttpResponse("非法请求，请登录操作")
    return HttpResponseRedirect(request.session['where_from'])


#数据上传
@login_required
def upname(request):
    username = request.user.username
    if request.method == 'POST':
        form = UpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                xlsfiles = request.FILES.get('upform', '')
                filename = xlsfiles.name
                fname = os.path.join(settings.MEDIA_ROOT, 'uploads/users/%s' % strftime("%Y/%m/%d", localtime()),filename)
                if os.path.exists(fname):
                    os.remove(fname)
                dirs = os.path.dirname(fname)
                if not os.path.exists(dirs):
                    os.makedirs(dirs)

                if os.path.isfile(fname):
                    os.remove(fname)
                content = xlsfiles.read()
                fp = open(fname, 'wb')
                fp.write(content)
                fp.close()#上传文件完成

                #删除旧数据

                Person.objects.all().delete()
                Result.objects.all().delete()
                #导入新数据
                book = xlrd.open_workbook(fname)
                sheet = book.sheet_by_index(0)
                for row_index in range(1, sheet.nrows):
                    record = sheet.row_values(row_index, 0)
                    try:
                        name = record[0].strip()
                        #phonenum = str(record[1]).rstrip(".0")
                        phonenum=int(record[1])

                        person = Person(name=name, tel=phonenum)
                        person.save()
                    except Person.DoesNotExist, e:
                        print e
                successinfo = "上传"
                success = True
                return HttpResponseRedirect('/')
                """
                return render_to_response('upname.html', {
                    "title": '导入人员名单',
                    'form': form,
                    'successinfo': successinfo,
                    'success': success,
                    'username': username}, context_instance=RequestContext(request))"""
            except Exception, e:
                print e
        else:
            return render_to_response('upname.html', {
                "title": '导入人员名单',
                'form': form,
                'username': username}, context_instance=RequestContext(request))
    return render_to_response('upname.html', RequestContext(request))


@csrf_exempt
def initialize(request):
    request.session['where_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method=='POST':

        Person.objects.all().update(isWin=0,mWin=0,cWin=1)
    else:
        return HttpResponse("非法请求")
    return HttpResponseRedirect(request.session['where_from'])


@login_required
def result(request):
    rst_obj=Result.objects.all()
    rst_5_1=rst_obj.filter(Q(awardname='五等奖'),Q(isdel=0)).order_by("-createtime")[:10]
    rst_5_2=rst_obj.filter(Q(awardname='五等奖'),Q(isdel=0)).order_by("-createtime")[10:20]

    rst_4=rst_obj.filter(Q(awardname='四等奖'),Q(isdel=0)).order_by("-createtime")[:6]
    rst_3=rst_obj.filter(Q(awardname='三等奖'),Q(isdel=0)).order_by("-createtime")[:3]
    rst_2=rst_obj.filter(Q(awardname='二等奖'),Q(isdel=0)).order_by("-createtime")[:2]
    rst_1=rst_obj.filter(Q(awardname='一等奖'),Q(isdel=0)).order_by("-createtime")[:1]
    rst_t=rst_obj.filter(Q(awardname='特等奖'),Q(isdel=0)).order_by("-createtime")[:1]
    rst_j=rst_obj.filter(Q(awardname='加奖'),Q(isdel=0)).order_by("-createtime")

    return render(request,'result.html',{'rst_5_1':rst_5_1 or None,
                                         'rst_5_2':rst_5_2 or None,
                                         'rst_4':rst_4 or None,
                                         'rst_3':rst_3 or None,
                                         'rst_2':rst_2 or None,
                                         'rst_1':rst_1 or None,
                                         'rst_t':rst_t or None,
                                         'rst_j':rst_j or None,
                                         })
