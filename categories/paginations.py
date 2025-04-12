from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 10

class TagPagination(PageNumberPagination):
    page_size = 10