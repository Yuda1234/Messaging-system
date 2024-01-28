from django.urls import path
from .views import WriteChetMessageView, GetChetMessagesView, GetUnreadChetMessagesView, ReadChetMessageView, \
    DeleteChetMessageView

urlpatterns = [
    path('write/', WriteChetMessageView.as_view(), name='write_chet_message'),
    path('get/', GetChetMessagesView.as_view(), name='get_chet_messages'),
    path('get_unread/', GetUnreadChetMessagesView.as_view(), name='get_unread_chet_messages'),
    path('read/<int:pk>/', ReadChetMessageView.as_view(), name='read_chet_message'),
    path('delete/<int:pk>/', DeleteChetMessageView.as_view(), name='delete_chet_message'),
]
