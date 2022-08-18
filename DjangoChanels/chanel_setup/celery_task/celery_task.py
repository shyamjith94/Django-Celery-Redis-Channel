import time
from ..socket.socket import notify_client
from celery import shared_task


@shared_task
def celery_info(info):
    """ Simple celery task it will wait 10 sec and send notification on web socket
    """
    print(info)
    time.sleep(10)
    notify_client(1)
    print("task complete")
