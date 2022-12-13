def check_is_admin(f):
    def wrapper(*args, **kwargs):

        if kwargs.get('username') != 'admin':
            raise Exception("Not allowed")


        return f(*args, **kwargs)
    return wrapper


class Store:
    storage = {
        'apple': 1,
        'banana': 2
    }

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)


store = Store()
print(store.get_food(username='customer', food='apple'))
print(store.get_food(username='admin', food='banana'))