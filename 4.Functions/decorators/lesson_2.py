def check_is_admin(f):
    print('decorator')
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("Not allowed")
        return f(*args, **kwargs)
    print('end decorator')
    return wrapper

class Store(object):
    storage = {
        'apple': 1,
        'banana': 2
    }

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

stor = Store()
print('code')
stor.get_food(username='admin', food='apple')


