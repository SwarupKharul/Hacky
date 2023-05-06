from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import HackathonSerializer
from .models import Hackathon


class HackathonListCreateView(ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        user = self.request.user
        # Only staff can create hackathons
        if user.is_staff:
            serializer.save(organizer=user)
        else:
            raise PermissionError("Only staff can create hackathons")

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Hackathon.objects.filter(organizer=user)
        return Hackathon.objects.all()


class HackathonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]


# View registered hackathons
@api_view(["GET"])
def registered_hackathons(request):
    user = request.user
    hackathons = Hackathon.objects.filter(participants=user)
    serializer = HackathonSerializer(hackathons, many=True)
    return JsonResponse(serializer.data, safe=False)


# participant can register for a hackathon
@api_view(["POST"])
def register_for_hackathon(request, pk):
    user = request.user
    hackathon_id = pk
    hackathon = Hackathon.objects.get(id=hackathon_id)
    hackathon.participants.add(user)
    return JsonResponse(
        {
            "status": "success",
            "message": "You have successfully registered for the hackathon",
        }
    )
