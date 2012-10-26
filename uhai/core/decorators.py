from django.core.exceptions import PermissionDenied

def permission_required(perm, login_url=None, raise_exception=False):
    def check_perms(user):
        if user.has_perm(perm):
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url=login_url)

def doctor_required(function=None, perm):
    actual_decorator = permission_required(
        perm,
        raise_exception=True
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
