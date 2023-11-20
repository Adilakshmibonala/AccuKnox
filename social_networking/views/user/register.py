from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status
from social_networking.models import User
from social_networking.serializers.validation_serializers.user import \
    RegisterUserRequestValidationSerializer


class RegisterUserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserRequestValidationSerializer

    @swagger_auto_schema(
        responses={
            200: "Success"
        },
        tags=["User"],
        operation_description="Register an user",
        operation_summary="Register an user",
        request_body=RegisterUserRequestValidationSerializer()
    )
    def create(self, request):
        request_data = request.data
        serializer = RegisterUserRequestValidationSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        email = request_data["email"].lower()
        user = User.objects.update_or_create(email=email, username=email, password=email)
        user.set_password(request_data['password'])
        user.save()

        return Response(data="Success", status=status.HTTP_200_OK)
