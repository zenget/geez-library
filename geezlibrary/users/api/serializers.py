from rest_framework import serializers
import datetime
from django.utils import timezone
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):

    borrowed_count = serializers.SerializerMethodField()
    due_for_return_in_30_days_count = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ('username', 'email','borrowed_count','due_for_return_in_30_days_count')

    def get_borrowed_count(self, instance):
        return instance.borrowed.filter(returned_date__isnull = True).count()

    def get_due_for_return_in_30_days_count(self, instance):
        return instance.borrowed.filter(returned_date__isnull = True,
        return_date__gte= timezone.now() + datetime.timedelta(days=15) ).count()

