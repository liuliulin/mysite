from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password)
        # print(username, password)
        temp = {"user": username, "pwd": password}
        # user_list.append(temp)
    user_list = models.UserInfo.objects.all()

    # return HttpResponse("hello world")
    return render(request, "index.html", {"data": user_list})


def page(request, index):
    page = index
    return HttpResponse("page: 第%s页" % page)


def page2(request, page, number):
    p = page
    n = number
    return HttpResponse("page: 第%s页 第%s条" % (p, n))


def home(request, user):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        print(type(user_list), user_list)
        return render(request, 't1.html', {'user_objs': user_list})
    else:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password)
        user_list = models.UserInfo.objects.all()
        return render(request, 't1.html', {'user_objs': user_list})