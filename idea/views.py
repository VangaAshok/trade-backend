from rest_framework import response
from .serializers import IdeaListSerializer, IdeaSerializer, IdeaSubscribeSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Idea
from rest_framework.decorators import action


# Create your views here.



class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "put", "get"]

    def get_serializer_class(self):
        if self.action == "update":
            return IdeaSubscribeSerializer
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = {"user": self.request.user}
        return super().get_serializer(*args, **kwargs)


class IdeaListViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaListSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    @action(detail=False, methods=["get"])
    def get_user_ideas(self, request):
        queryset = self.get_queryset().filter(created_by=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Idea.objects.select_related("created_by").all()

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = {"user": self.request.user}
        return super().get_serializer(*args, **kwargs)
