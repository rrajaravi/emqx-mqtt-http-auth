from django.urls import path

from .views import WebHookView, AuthView

v1patterns = [
    path('webhook', WebHookView.as_view(), name='web-hook'),
    path('auth', AuthView.as_view(), name='auth-view'),
    path('acl', AuthView.as_view(), name='acl-view')
]
