import hashlib
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.userTools import make_token
from user.models import UserProfile


def users(request):
    # 创建数据
    if request.method == "POST":
        # 获取用户名
        json_str = request.body
        if not json_str:
            result={'code':100,'error':'no body'}
            return JsonResponse(result)
        #json字符串转换为json对象
        json_obj = json.loads(json_str.decode())
        username = json_obj.get('username','')
        print(username)
        # 获取密码
        password1 = json_obj.get('password_1','')
        password2 = json_obj.get('password_2','')
        # 获取邮箱
        email = json_obj.get('email', '')
        # 获取用户属性
        usertype = json_obj.get('usertype', '')
        if not username:
            result = {
                "code": 101,
                "error": 'no username'
            }
            return JsonResponse(result)
        if not password1 or not password2:
            result = {
                "code": 102,
                "error": 'no password'
            }
            return JsonResponse(result)
        if not email:
            result = {
                "code": 103,
                "error": 'no email'
            }
            return JsonResponse(result)
        if not usertype:
            result = {
                "code": 104,
                'error': 'no usertype'
            }
            return JsonResponse(result)
        if password1 != password2:
            result = {
                'code': 105,
                'error': 'password is not same'
            }
            return JsonResponse(result)
        if usertype not in ('1', '2', '3'):
            result = {
                'code': 106,
                'error': 'usertype is wrong'
            }
            return result
        # 检查数据库中是否存在该用户
        auer = UserProfile.objects.filter(username=username)
        if auer:
            result = {'code': 107, 'error': 'user already exits'}
            return JsonResponse(result)
        # 处理密码,对密码采用Md5加密
        pwd = hashlib.md5()
        pwd.update(password1.encode())
        # 加密后的密码
        newpwd = pwd.hexdigest()
        # 创建用户
        try:
            UserProfile.objects.create(
                username=username,
                password=newpwd,
                email=email,
                usertype=usertype)
        except:
            reuslt = {'code': 108, 'error': 'create fail'}
            return JsonResponse(reuslt)
        # 创建token----以下方法采用token
        token = make_token(username=username).decode()
        data = {
            'token': token
        }
        result = {'code': 200, 'username': username, 'data': {"token": token}}
        return JsonResponse(result)
    # return JsonResponse({'code':200,'result':{'data':'hahhah'}})
