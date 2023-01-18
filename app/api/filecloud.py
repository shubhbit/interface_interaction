from filecloud_admin import FileCLoudAdmin
from filecloud_user import FileCloudUser


class FileCloud(object):
    class_type = {"admin": FileCLoudAdmin, "user": FileCloudUser}

    @staticmethod
    def get_instance(type):
        return FileCloud.class_type[type]()
    
