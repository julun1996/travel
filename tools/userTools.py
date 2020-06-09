import time

import jwt

from tools.config import config


def make_token(username):
    """
    注册或者登录时,根据用户名创建token
    :param username: 用户名
    :return:
    """
    # 加密key值
    key = config.Config.KEY
    # token有限时长
    expire = config.Config.EXPIRE
    now = time.time()
    # 入参
    payload = {'username': username, 'exp': int(now + expire)}
    #生成token
    token = jwt.encode(payload=payload, key=key, algorithm='HS256')
    return token
