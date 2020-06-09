"""
此模块用于校验token
@author by julun
@date: 2020/06/06 08:08
"""
import jwt
from django.http import JsonResponse
from tools.config.config import Config

from user.models import UserProfile


key =Config.KEY
def check_token(*method):
    def _login_check(func):
        def wapper(request, *args, **kwargs):
            # 通过request检查token
            # 校验不通过,return JsonHttpResponse
            token = request.META.get('HTTP_AUTHORIZATION')
            # !!!!这里判断请求方式很巧妙
            if request.method not in method:
                return func(request, *args, *kwargs)
            if not token:
                result = {'code': 107, 'error': 'Please login'}
                return JsonResponse(result)
            try:
                res = jwt.decode(token, key=key, algorithms=['HS256'])
            except jwt.ExpiredSignatureError as e:
                result = {'code': 108, 'error': 'Please login'}
            except Exception as e:
                result = {'code': 109, 'error': 'Please login'}

            username = res['username']
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                user = None
            if not user:
                result = {'code': 110, 'error': 'no user'}
                return JsonResponse(result)
            # 万物皆对象
            request.user = user

            return func(request, *args, **kwargs)

        return wapper

    return _login_check
