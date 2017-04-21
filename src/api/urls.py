from box.api import views as box_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('box/box', box_views.BoxViewSet)
router.register('box/items', box_views.ItemViewSet)
router.register('box/users', box_views.UserViewSet)
router.register('box/activities', box_views.ActivityViewSet, 'activities')
router.register('box/rfid', box_views.RFIDViewSet, 'rfid')
router.register('box/weight', box_views.WeightViewSet, 'weight')
router.register('box/events', box_views.EventViewSet, 'events')

urlpatterns = router.urls
