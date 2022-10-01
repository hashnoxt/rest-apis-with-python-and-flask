from resources.user import User


def authenticate(username, password):
    user = User.find_by_username(username)  # username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)  # userid_mapping.get(user_id, None)
