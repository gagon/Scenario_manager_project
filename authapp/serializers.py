from rest_framework import serializers
from .models import User


class CurrentUserWellsSerializer(serializers.ModelSerializer):
    well = serializers.HyperlinkedRelatedField(
        many=True, view_name="well_detail", queryset=User.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "well"]