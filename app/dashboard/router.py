import dashboard.models


my_tables = [cls for cls in dashboard.models.__dict__.values() if isinstance(cls, type)]

class MyDbRouter(object):
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    def db_for_read(self, model, **hints):
        "Point all operations on dashboard models to 'ip_core'"
        if model in my_tables:
            return 'ip_core'
        return None