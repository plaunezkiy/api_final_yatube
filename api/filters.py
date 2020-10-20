from django.shortcuts import get_object_or_404
from rest_framework.filters import BaseFilterBackend
from .models import Group


class PostsByGroupFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            group = get_object_or_404(Group, pk=request.GET['group'])
        except:
            return queryset
        return queryset.filter(group=group)

