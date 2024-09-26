from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    # Authenticated users only can see list view
    if request.user.is_authenticated:
      return True
    return False

  def has_object_permission(self, request, view, obj):
    # Read peermissons are allowed to any request so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
      return True

    # Write permissions are only allowed to the owner of the content
    return obj.owner == request.user