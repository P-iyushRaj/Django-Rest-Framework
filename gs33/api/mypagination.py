from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=6
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    #http://127.0.0.1:8000/studentapi/?mylimit=4&myoffset=8
    max_limit =7
    