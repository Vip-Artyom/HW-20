import calendar
import datetime

from flask_restx import abort

from constants import SECRET_KEY, ALGORITHM
import jwt


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_user_by_username(username)

        if not user:
            abort(404)

        if is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role,
            "password": password
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=SECRET_KEY, algorithms=ALGORITHM)

        username = data.get("username")
        password = data.get("password")

        return self.generate_tokens(username, password, is_refresh=True)

    def check_token(self, token):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
            return True
        except Exception as e:
            print(e)
            return False
