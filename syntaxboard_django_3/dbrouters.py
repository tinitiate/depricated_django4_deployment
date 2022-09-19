from django.conf import settings

class AppRouter:

    def db_for_read(self, model, **hints):
        """
        SET DB Connection for Apps
        """
        if model._meta.app_label == 'usermanagement':
           return 'LOANS'
        elif model._meta.app_label == 'models':
           return 'LOANS'
        elif model._meta.app_label == 'webservices_db':
           return 'LOANS'
        else:
            return 'default'

        return None 


    def db_for_write(self, model, **hints):
        """
        SET DB Connection for Apps
        """
        if model._meta.app_label == 'usermanagement':
           return 'LOANS'
        elif model._meta.app_label == 'models':
           return 'LOANS'
        elif model._meta.app_label == 'webservices_db':
           return 'LOANS'
        else:
           return 'default'

        return None


    def allow_relation(self, obj1, obj2, **hints):
        """
        SET DB Connection for Apps
        """
        if obj1._meta.app_label == 'usermanagement' or \
           obj2._meta.app_label == 'usermanagement':
           return True
        elif obj1._meta.app_label == 'models' or \
           obj2._meta.app_label == 'models':
           return True
        elif obj1._meta.app_label == 'webservices_db' or \
           obj2._meta.app_label == 'webservices_db':
           return True
        else:
           return True

        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        SET DB Connection for Apps
        """
        if app_label == 'usermanagement':
           return 'LOANS'
        elif app_label == 'models':
           return 'LOANS'
        elif app_label == 'webservices_db':
           return 'LOANS'
        else:
           return 'default'

        return None
