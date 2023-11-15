from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset=Advertisement.objects.all()
    serializer_class=AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_class = AdvertisementFilter
    filter_fields=['id', 'creator', 'created_at', 'status']
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
