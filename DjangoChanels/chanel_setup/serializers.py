from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetailsSerializers(ModelSerializer):
    """ Serializer for return all user details
    """

    class Meta:
        model = User
        exclude = ["password"]
