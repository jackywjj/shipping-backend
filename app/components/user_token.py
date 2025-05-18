import hashlib
from datetime import timedelta, datetime

import jwt
from jwt.exceptions import ExpiredSignatureError

from app.models.user import User

EXPIRED_HOUR = 30


class UserToken(object):
    key = 'aUgsFk96LsAMU5c2Zx'
    salt = 'nk12PYxCwz69sayh'

    @staticmethod
    def generate_token(user: User):
        headers = dict(typ="jwt", alg="HS256")
        payload = dict({"user_id": user.id, "exp": datetime.now() + timedelta(hours=EXPIRED_HOUR)})
        return jwt.encode(payload=payload, key=UserToken.key, algorithm="HS256", headers=headers)

    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key, algorithms=['HS256'])
        except ExpiredSignatureError:
            raise Exception("token已过期, 请重新登录")

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        bt = f"{password}{UserToken.salt}".encode("utf-8")
        m.update(bt)
        return m.hexdigest()
