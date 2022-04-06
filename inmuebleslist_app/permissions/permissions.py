from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission (self,request,view):
       
        if request.method =='GET':
            return True
        
        stuff=bool(request.user and request.user.is_staff)
        return stuff
        