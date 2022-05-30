import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d["password"] = self.get_hash(user_d["password"])
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d["password"] = self.get_hash(user_d["password"])
        return self.dao.update(user_d)

    def delete(self, rid):
        self.dao.delete(rid)
        
    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "id" in data:
            user.id = data["id"]
        if "username" in data:
            user.username = data["username"]
        if "password" in data:
            user.password = self.get_hash(data["password"])
        if "role" in data:
            user.role = data["role"]

        self.dao.update_partial(user)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS)
        )

    def get_user_by_username(self, username):
        return self.dao.get_user_by_username(username)

    def compare_password(self, password_hash, other_password):
        return hmac.compare_digest(password_hash, self.get_hash(other_password))
