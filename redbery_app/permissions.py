from rest_framework import permissions

class IsBlogPermisshion(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return request.method == 'GET'
        return request.method in ['GET', 'POST']
    


class IsCategoryPermisshion(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
        
     
   