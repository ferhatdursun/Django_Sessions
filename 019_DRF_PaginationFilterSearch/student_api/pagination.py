from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class MyPageNumberPagination(PageNumberPagination):
    page_size = 15 # size per page
    page_query_param = 'sayfa' # change page variable.
    page_size_query_param = 'limit' # change page_size from url.

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10 # default limit.
    max_limit = 99
    limit_query_param = 'adet' # change "limit" variable.
    offset_query_param = 'haric' # change "offset" variable.

class MyCursorPagination(CursorPagination):
    ordering = '-last_name' # sort.
    page_size = 10
    page_query_param = 'cursor' # change "cursor" variable.
