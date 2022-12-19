from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def get_inline_instances(self, request, obj=None):
        if not obj or obj.date >= today: return []
        return super(IsAdmin, self).get_inline_instances(request, obj)



class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user == "manager"



class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user == "user"