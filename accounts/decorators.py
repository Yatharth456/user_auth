from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def get_inline_instances(self, request, obj=None):
        print("aaaaaaadsfghjhfgfdds")
        if not obj or obj.date >= today: return []
        return super(IsAdmin, self).get_inline_instances(request, obj)



class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user == "manager"



class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user == "user"


from rest_framework import permissions

class CustomerAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'
    print("adsfdgfhgjghhh=zzzzz==========")
    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        # print("YDRHRDHGFTFUYG")
        print(request.user.role)
        # print(request)
        return True
        print(request.user.is_authenticated)
        return (request.user and request.user.is_authenticated)

'''
 ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

'''

'''


'''
class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "1":
            return True
        return False

class ManagerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "2":
            return True
        return False