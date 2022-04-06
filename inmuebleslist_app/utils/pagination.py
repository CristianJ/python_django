from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class EdificacionPagination(PageNumberPagination):
    page_size =3
    page_size_query_param='size'
    max_page_size=10
    #last_page_strings='end'
    
    
class EdificacionPaginationOffset(LimitOffsetPagination):
    default_limit=1