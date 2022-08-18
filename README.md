# Django-Celery-Redis-Channel
# setup for django, celery,redis, websocket communication run in docker new version 

# How To Run
* install docker make sure running background
* run command "docker compose -f docker_compose.yaml up"
    docker will pull and create django celery redis instances
* docker will run redis broker redis:6379/1, for celery redis:6379/2
* django will run 127.0.0.1:5000

# Api Call
* keep connection on web socket using ws://127.0.0.1:5000/ws/subscribe/user/1/
* Make api call 127.0.0.1:5000/api/user/, it returns a response object and initiate celery job
* after 10 sec get web socket message task complete.

# Setup Details Celery
    DjangoChanels/celery        -> creating celery app
    DjangoChanels/__init__      -> distibuting to django app
    DjangoChanels/celery_task   -> simple task for celry
    DjangoChanels/setting       -> celery settings

# Setup Details WS
    DjangoChanels/asgi      -> creating asgi app
    DjangoChanels/routing   -> ws urls
    DjangoChanels/consumers -> ws consummers 
    DjangoChanels/socket    -> ws notification setup
    DjangoChanels/setting   -> ws settings
