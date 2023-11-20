from rest_framework import serializers


class RegisterUserRequestValidationSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"
