class User(object):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    @classmethod
    def from_dict(cls, user_dict):
        """Create an object from a dict"""
        id = user_dict['id']
        username = user_dict['username']
        password = user_dict['password']
        role = user_dict['role']
        return cls(id, username, password, role)

    def __iter__(self):
        return iter([('id', self.id), \
                     ('username', self.username), \
                     ('password', self.password), \
                     ('role', self.role)])

    def __str__(self):
        return 'User id:{}, name:{}, role:{}'.format(self.id, self.username, self.role)

