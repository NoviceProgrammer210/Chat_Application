import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # 👇 import inside the URLRouter to delay it
            __import__('chat.routing').routing.websocket_urlpatterns +
            __import__('room.routing').routing.websocket_urlpatterns
        )
    ),
})
