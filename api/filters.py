from rest_framework import filters
from django.db.models import Q


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allow users to see their own objects
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)


class IsPublicFilterBackend(filters.BaseFilterBackend):
    """
    Filter that allow users to see public objects
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(isPublic=True)


class IsOwnerOrPublicFilterBackend(filters.BaseFilterBackend):
    """
    Filter combine two above together
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(Q(owner=request.user) | Q(isPublic=True))
