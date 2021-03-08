from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'
    page_size_query_param = 'records' #user can decide page size
    max_page_size = 7
    last_page_strings = 'end'
    #http://127.0.0.1:8000/studentapi/?p=end&records=6

    