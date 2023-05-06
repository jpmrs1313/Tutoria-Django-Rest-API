import django_filters
from .models import CustomUser, Teacher, Student


class UserBaseFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr="icontains")
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name",
        ]


class StudentFilter(UserBaseFilter):
    number = django_filters.NumberFilter(lookup_expr="exact")
    teacher = django_filters.NumberFilter(lookup_expr="exact")

    class Meta:
        model = Student
        fields = UserBaseFilter.Meta.fields + [
            "number",
            "teacher",
        ]


class TeacherFilter(UserBaseFilter):
    number = django_filters.NumberFilter(lookup_expr="exact")
    teacher = django_filters.NumberFilter(lookup_expr="exact")

    class Meta:
        model = Teacher
        fields = UserBaseFilter.Meta.fields + [
            "number",
        ]
