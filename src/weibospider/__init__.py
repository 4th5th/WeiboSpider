__all__ = ['context', 'BreadthFirstWeiboProvider', 'WeiboModel', 'UserModel']

class BreadthFirstWeiboProvider(object):
    
    WEIBO_COUNT = 500
    
    def __init__(self, weiboAPI, context):
        self._weiboAPI = weiboAPI
        self._context = context
    
    def getWeibos(self):
        user = self._context.dequeueUser()
        while user is not None:
            for weibo in self._weiboAPI.getWeibo(user.name, BreadthFirstWeiboProvider.WEIBO_COUNT):
                yield weibo
            else:
                userList = self._weiboAPI.getFollowingUser(user.name)
                saveUserList = [x for x in userList if not self._context.existsUser(x.name)]
                self._context.enqueueUsers(saveUserList)
                user = self._context.dequeueUser()
        else:
            raise StopIteration
            

class WeiboModel(object):
    def __init__(self):
        self.userName = None
        self.text = None
        self.retweetedText = None
        self.time = None
        self.id = None

class UserModel(object):
    def __init__(self):
        self.name = None
