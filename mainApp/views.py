from rest_framework import generics
from .models import History
from .serializers import HistorySerializer,HistoryupdateSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=History.objects.all()
    serializer_class=HistoryupdateSerializer
    def delete(self, request, pk=None,*args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
