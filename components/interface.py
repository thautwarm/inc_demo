from abc import abstractmethod


class UserParser:
    @abstractmethod
    def __init__(self, user):
        """
        """

    @abstractmethod
    def get_user_info(self):
        """

        :param user:
        :return: {
            username: 用户名
            number: 学号或工号
            avatar: 头像
        }
        """


class DefaultUserParser(UserParser):
    def __init__(self, user):
        self.user = user

    def get_user_info(self):
        user = self.user
        return user['username'], user['number'], user['avatar']
