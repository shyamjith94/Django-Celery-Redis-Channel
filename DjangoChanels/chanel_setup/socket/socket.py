import channels.layers
from asgiref.sync import async_to_sync


class BaseSocketDatagram:
    """
    base class
    """
    CHANNEL_LAYER = channels.layers.get_channel_layer()
    PIP = "initial_data"
    FLOW_CONTROL = 1

    def __init__(self, user=None, data={}, *args, **kwargs):
        self.user = user
        self.data = data

    def payload(self):
        """
        :return {}
        """
        data = {
            'message': None,
            'data': None
        }
        return data

    @property
    def channel_layer(self):
        """
        :return str
        """
        return self.CHANNEL_LAYER

    def get_datagram(self):
        """
        :return {}
        """
        data = {
            'type': self.PIP,
            'flow_control': self.FLOW_CONTROL,
            'payload': self.payload()}
        return data

    @property
    def channel_name(self):
        """
        :return str
        """
        return f"user_{getattr(self.user, 'id', '0')}"

    def send(self):
        """
        :return {}
        """
        datagram = self.get_datagram()
        return async_to_sync(self.channel_layer.group_send)(self.channel_name, datagram)


class TestSocket(BaseSocketDatagram):
    """
    test socket works
    """
    PIP = "notification_pipe"

    def __init__(self, id, data=None, user=None):
        self.id = id
        super().__init__(data=data, user=user)

    @property
    def channel_name(self):
        """
        construct channel name
        """
        return f"test_{self.id}"

    def payload(self):
        """
        creating payload
        """
        data = {
            "message": "celery task complete",
            'data': None
        }
        return data


def notify_client(id: int, info="") -> None:
    """
    :return: None
    """

    payload = TestSocket(id)
    payload.send()
