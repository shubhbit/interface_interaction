
class FileCloudBase(object):
    def __init__(self):
        self.cookies = None

    @staticmethod
    def build_url(url, query):
        for indx, key in enumerate(query):
            if indx == 0:
                url += "?{}={}".format(key, query[key])
            else:
                url += "&{}={}".format(key, query[key])
        return url

    @staticmethod
    def authenticated(func):
        def check_auth(*args):
            if args[0].cookies:
                response = func(*args)
                return response
            else:
                raise Exception(
                    "User is not authenticated to perform this operation")
        return check_auth
