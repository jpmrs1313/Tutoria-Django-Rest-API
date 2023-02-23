import django_filters
from teachers.models import Teacher

class TeacherFilter(django_filters.FilterSet):
    number = django_filters.NumberFilter(lookup_expr='exact')
    user__email = django_filters.CharFilter(lookup_expr='icontains')
    user__first_name = django_filters.CharFilter(lookup_expr='icontains')
    user__last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['number', 'user__email', 'user__first_name', 'user__last_name']