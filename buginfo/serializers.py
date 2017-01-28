from rest_framework import serializers
from buginfo.models import  BugInfo

class BugInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugInfo
        fields = ('title','url', 'info', 'owner', 'status', 'public')
