from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'
    cursor_query_param = 'cu'
    #http://127.0.0.1:8000/studentapi/?cu=cD1nZ2c%3D
    