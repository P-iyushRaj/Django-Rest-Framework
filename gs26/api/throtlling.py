#different no. of throttle for different class view
#AnonThrottle rate is same for all class view

from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
    
