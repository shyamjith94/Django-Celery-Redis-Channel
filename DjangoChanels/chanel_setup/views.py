from rest_framework.generics import GenericAPIView, RetrieveAPIView
from .serializers import UserDetailsSerializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .celery_task.celery_task import celery_info

# Create your views here.

User = get_user_model()


class UserDetailsView(GenericAPIView):
    """
    Simple api view
    """
    serializer_class = UserDetailsSerializers
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Add one celery task on request
        :return Response
        """
        celery_info.delay("started celery  task")
        all_users = self.get_queryset()
        ser = self.get_serializer(all_users, many=True)
        data = {
            "message": 'celery task has on going',
            "data": ser.data}
        return Response(data)
