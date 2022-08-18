from django.urls import re_path
from .consumers import CommonConsumer


websocket_urlpatterns = [
    re_path(
        r"ws/subscribe/user/(?P<id>\w+)/$", CommonConsumer.as_asgi()
    ),
]