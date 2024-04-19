from django import template

register = template.Library()

@register.filter(name='has_permission')
def has_permission(user, permission):
    print(f'User Has Persmisson: {user.has_perm(permission)}')
    return user.has_perm(permission)
