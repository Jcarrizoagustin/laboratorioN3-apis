from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
        Permiso personalizado que permite a un SUPER USUARIO realizar cualquier acción (C-R-U-D)
        Para un USUARIO COMÚN  sólo permite Visualizar
    """
    
    #Método a nivel de Vista
    def has_permission(self, request, view):
        
        #Permitir todas las acciones (SuperUser)
        if request.user and request.user.is_superuser:
            return True
        

        #Permitir acción solo lectura (User)
        return request.method in permissions.SAFE_METHODS


    #Método a nivel de Objectos
    def has_object_permission(self, request, view, obj):
        
        #Permitir todas las acciones (SuperUser)
        if request.user and request.user.is_superuser:
            return True
        
        # Permitir acciones de lectura para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permitir la edición solo si el usuario es el propietario del objeto
        return obj.owner == request.user