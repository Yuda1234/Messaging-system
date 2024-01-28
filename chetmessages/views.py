from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ChetMessage
from .serializers import ChetMessageSerializer


class WriteChetMessageView(generics.CreateAPIView):
    serializer_class = ChetMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class GetChetMessagesView(generics.ListAPIView):
    serializer_class = ChetMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChetMessage.objects.filter(receiver=self.request.user)


class GetUnreadChetMessagesView(generics.ListAPIView):
    serializer_class = ChetMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChetMessage.objects.filter(receiver=self.request.user, is_read=False)


class ReadChetMessageView(generics.RetrieveAPIView):
    serializer_class = ChetMessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return ChetMessage.objects.filter(receiver=self.request.user)


class DeleteChetMessageView(generics.DestroyAPIView):
    serializer_class = ChetMessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return ChetMessage.objects.filter(sender=self.request.user) | ChetMessage.objects.filter(
            receiver=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


