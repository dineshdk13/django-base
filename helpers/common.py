from mybase.settings import USER_ROLES
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
import random
import datetime
# from myapps.one.models import CustomUser
import time

def group_user(user,user_role):
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

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def get_random(len):
    random_length = len #len of random value
    possible_values = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random_list = [random.choice(possible_values) for i in range(random_length)]
    random_value = "".join(random_list)
    return random_value

def timeAgo(time_ago):
    time_ago = datetime.datetime.strptime(str(time_ago)[:19],'%Y-%m-%d %H:%M:%S')
    cur_time   = datetime.datetime.now()
    time_elapsed   = (cur_time - time_ago).total_seconds()
    seconds    = time_elapsed
    
    minutes    = round( time_elapsed / 60 ) 
    hours      = round( time_elapsed / 3600 )
    days       = round( time_elapsed / 86400 )
    weeks      = round( time_elapsed / 604800 )
    months     = round( time_elapsed / 2600640 )
    years      = round( time_elapsed / 31207680 )

    # print(months,"test")
    # raise SystemExit
    # exit()
    
    #Seconds
    if(seconds <= 60):
        return "just now"
    
    #Minutes
    elif(minutes <=60):
        if(minutes==1):
            return "one minute ago"
        else:
            return f"{minutes} minutes ago"
        
    #Hours
    elif(hours <=24):
        if(hours==1):
            return "an hour ago"
        else:
            return f"{hours} hrs ago"

    #Days
    elif(days <= 7):
        if(days==1):
            return "yesterday"
        else:
            return f"{days} days ago"

    #Weeks
    elif(weeks <= 4.3):
        if(weeks==1):
            return "a week ago"
        else:
            return f"{weeks} weeks ago"
        
    #Months
    elif(months <=12):
        if(months==1):
            return "a month ago"
        else:
            return f"{months} months ago"
        
    #Years
    else:
        if(years==1):
            return "one year ago"
        else:
            return f"{years} years ago"

"""same method as above with time_ago library"""
# to use "pip install timeago"
# def timeAgo(time_ago):
#     time_ago = datetime.datetime.strptime(str(time_ago)[:19],'%Y-%m-%d %H:%M:%S')
#     cur_time = datetime.datetime.now()
#     time_ago = timeago.format(time_ago, cur_time)
#     # time_ago = time_ago.replace("months", "mon")
#     return time_ago

#convert unix timestamp to readable format
def convert_epoch_to_dt(date):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))