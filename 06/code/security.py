<<<<<<< HEAD

from resources.user import User


def authenticate(username, password):
    user = User.find_by_username(username)  # username_mapping.get(username, None)

=======
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)  # username_mapping.get(username, None)
>>>>>>> a0b222b (server/app : final commit)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
<<<<<<< HEAD

    return User.find_by_id(user_id)  # userid_mapping.get(user_id, None)

=======
    return UserModel.find_by_id(user_id)  # userid_mapping.get(user_id, None)
>>>>>>> a0b222b (server/app : final commit)
