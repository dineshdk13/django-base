from mybase.settings import USER_ROLES
from django.contrib.auth.models import Group

def user_group(user,user_role):
    try:
        have_value = Group.objects.filter().exists()

        #initializing name for groups from USER_ROLES if table is empty
        if not have_value:
            for role in USER_ROLES:
                group = Group(name=role)
                group.save()
        AdminRole = Group.objects.filter(name=user_role).first().id
        user.groups.add(AdminRole) # Add User to admin group
        return True
    except Exception as e:
        print (e)
        return False

def get_user_role(user):
    group_name =  user.groups.values_list('name', flat=True).first()
    return group_name
