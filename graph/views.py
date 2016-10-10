import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def Upload(request):
    if request.method == "POST":
        # id = request.GET['kw']
        # ids = Check.objects.filter(id=id)
        db = UserForm(request.POST, request.FILES)
        if db.is_valid():
            headImg = db.cleaned_data['headImg']
            username = db.cleaned_data['username']
            kap = db.cleaned_data['kap']
            C_lass = db.cleaned_data['C_lass']

            user = User()
            user.headImg = headImg
            user.username = username
            user.kap = kap
            user.C_lass = C_lass
            user.save()
            return render(request, 'ok.html')
    else:
        db = UserForm()
    return render(request, 'upload.html', {'db': db})


#
# def Checkupload(request):
#     if request.method == "POST":
#         db = CheckForm(request.POST, request.FILES)
#         if db.is_valid():
#             headImg = db.cleaned_data['headImg']
#             username = db.cleaned_data['username']
#             kap = db.cleaned_data['kap']
#             C_lass = db.cleaned_data['C_lass']
#
#             check = Check()
#             check.headImg = headImg
#             check.username = username
#             check.kap = kap
#             check.C_lass = C_lass
#             check.save()
#             return HttpResponse('ok')
#     else:
#         db = UserForm()
#     return render(request, 'check.html', {'db': db})


def Checked(request):
    global id, headImg, imgid, C_lass, kap, username, imgurl
    objects = User.objects.all()
    limit = 1
    p = Paginator(objects, limit)
    page = request.GET.get('page')
    try:
        cd = p.page(page)
    except PageNotAnInteger:
        cd = p.page(1)
    except EmptyPage:
        cd = p.page(p.num_pages)

    for i in cd:
        headImg = str(i.headImg)
        imgurl = i.headImg.url
        username = i.username
        kap = i.kap
        C_lass = i.C_lass
    if request.POST.get('ok'):
        check = Check()
        check.headImg = imgurl
        check.username = username
        check.kap = kap
        check.C_lass = C_lass
        check.save()

        pinglun = Pinglun()
        imgidlist = Check.objects.filter(Q(username=username, headImg=imgurl, kap=kap, C_lass=C_lass))
        for i in imgidlist:
            imgid = i.id
        pinglun.index = imgid
        pinglun.cai = 0
        pinglun.zan = 0
        pinglun.save()
        User.objects.filter(headImg=headImg).delete()
        return HttpResponse('ok')
    if request.POST.get('delete'):
        deleteimg(headImg)
        User.objects.filter(headImg=headImg).delete()
        return HttpResponse('delete')

    return render(request, 'check.html', {'cd': cd})


def index(request):
    objects = Check.objects.all()[::-1]
    imgidobj = Pinglun.objects.all()[::-1]
    limit = 20
    p = Paginator(objects, limit)
    page = request.GET.get('page')

    try:
        db = p.page(page)
    except PageNotAnInteger:
        db = p.page(1)
    except EmptyPage:
        db = p.page(p.num_pages)

    l3 = zip(db, imgidobj)
    return render(request, 'index.html', {'l3': l3})


def search(request):
    limit = 20
    kw = request.GET['user_search']
    object = Check.objects.filter(Q(C_lass__contains=kw) | Q(username__contains=kw) | Q(kap__contains=kw))
    imgidobj = []
    for i in object:
        asdf = Pinglun.objects.filter(index=i.id)
        for x in asdf:
            imgidobj.append({"id": x.id, "index": x.index, "zan": x.zan, "cai": x.cai})
    page = request.GET.get('page')

    if len(object) == 0:
        return render(request, 'error.html', {'kw', kw})
    else:
        if len(object) < 20:
            l3 = zip(object, imgidobj)
            return render(request, 'search20.html', {'l3': l3, 'kw': kw})
        else:
            p = Paginator(object, limit)
            try:
                db = p.page(page)
            except PageNotAnInteger:
                db = p.page(1)
            except EmptyPage:
                db = p.page(p.num_pages)
            l3 = zip(db, imgidobj)
            return render(request, 'search.html', {'l3': l3, 'kw': kw})


def uploadlist(request):
    global Qset
    uploadlist = Check.objects.all()
    list = []
    check1 = []
    for i in uploadlist:
        check1.append([i.username, i.kap, i.C_lass])

    check2 = []
    for i in range(0, len(check1)):
        if check1[i] not in check2:
            check2.append(check1[i])
    # print(check2)

    for x in check2:
        uploadid = Check.objects.filter(Q(username=x[0], kap=x[1], C_lass=x[2]))
        idlist = []
        for y in uploadid:
            idlist.append(y.id)
        list.append(max(idlist))

    outputlist = []
    for z in list:
        Qset = Check.objects.filter(id=z)
        for i in Qset:
            outputlist.append([i.headImg, i.username, i.kap, i.C_lass])
    limit = 30
    page = request.GET.get('page')
    p = Paginator(outputlist, limit)
    try:
        db = p.page(page)
    except PageNotAnInteger:
        db = p.page(1)
    except EmptyPage:
        db = p.page(p.num_pages)

    return render(request, 'uploadlist.html', {'outputlist': db})


def inside_view(request):
    name = request.GET['name']
    C_LASSS = request.GET['class']
    kap = request.GET['kap']
    db = Check.objects.filter(Q(username=name, C_lass=C_LASSS, kap=kap))[::-1]
    return render(request, 'content.html', {'db': db})


def uploadsearch(request):
    global Qset
    kw = request.GET['upload_search']
    uploadlist = Check.objects.filter(Q(C_lass__contains=kw) | Q(username__contains=kw) | Q(kap__contains=kw))
    list = []
    check1 = []
    for i in uploadlist:
        check1.append([i.username, i.kap, i.C_lass])

    check2 = []
    for i in range(0, len(check1)):
        if check1[i] not in check2:
            check2.append(check1[i])
    # print(check2)

    for x in check2:
        uploadid = Check.objects.filter(Q(username=x[0], kap=x[1], C_lass=x[2]))
        idlist = []
        for y in uploadid:
            idlist.append(y.id)
        list.append(max(idlist))

    outputlist = []
    for z in list:
        Qset = Check.objects.filter(id=z)
        for i in Qset:
            outputlist.append([i.headImg, i.username, i.kap, i.C_lass])
    limit = 30
    page = request.GET.get('page')
    p = Paginator(outputlist, limit)
    try:
        db = p.page(page)
    except PageNotAnInteger:
        db = p.page(1)
    except EmptyPage:
        db = p.page(p.num_pages)

    return render(request, 'uploadlist.html', {'outputlist': db})


def deleteimg(headImg):
    filename = 'D:/website/Photo/Media/' + headImg
    if os.path.exists(filename):
        os.remove(filename)


def zan(request):
    index = request.GET.get('id')
    count = request.GET.get('count')
    id = Pinglun.objects.filter(index=index)
    id.update(zan=int(count) + 1)
    return HttpResponse(True)


def cai(request):
    index = request.GET.get('id')
    count = request.GET.get('count')
    id = Pinglun.objects.filter(index=index)
    id.update(cai=int(count) + 1)
    return HttpResponse(True)


def hot(request):
    all = Pinglun.objects.all()
    indexlist = []
    for x in all:
        indexlist.append(x.zan)
    bigg = []
    while True:
        if len(indexlist) == 0:
            break
        if len(indexlist) > 10:
            indexlist.remove(min(indexlist))
        if len(indexlist) <= 10:
            bigg.append(max(indexlist))
            indexlist.remove(max(indexlist))

    bigggg = []
    biggimg = []
    for v in bigg:
        asdf = Pinglun.objects.filter(zan=v)
        for x in asdf:
            bigggg.append({"id": x.id, "index": x.index, "zan": x.zan, "cai": x.cai})
            asdf = Check.objects.filter(id=x.index)
            for x in asdf:
                biggimg.append(
                    {"id": x.id, "headImg": x.headImg, "username": x.username, "kap": x.kap, "C_lass": x.C_lass})

        l3 = zip(biggimg, bigggg)
    return render(request, "hot.html", {"l3": l3})


# def geting(request):
#     id = request.GET.get('id')
#     img = Check.objects.filter(id=id)
#     for i in img:
#         imgsrc = i.headImg
#     return render(request,"img.html",{"imgsrc":imgsrc})



def P_inglun(request):
    index = request.GET.get('index')
    comment = Comment.objects.filter(index=index)
    return render(request, "Pinglun.html", {"comment": comment})


def addPinglun(request):
    index = request.GET.get('id')
    comment = request.GET.get('c')
    asdf = Comment()
    asdf.floor = 1
    asdf.index = index()
    asdf.pinglun = comment
    asdf.save()


def ajaxindex(request):
    page = request.GET.get('page')
    hanzai = int(page) * 2
    limit = 20
    objects = Check.objects.all()[hanzai::-1]
    imgidobj = Pinglun.objects.all()[hanzai::-1]
    p = Paginator(objects, limit)
    db = p.page(page)
    l3 = zip(db, imgidobj)
    return render(request, 'indexajax.html', {'l3': l3})
