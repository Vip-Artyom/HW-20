import hashlib

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
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)

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
            user.password = data["password"]
        if "role" in data:
            user.role = data["role"]

        self.dao.update_partial(user)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
