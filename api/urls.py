from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments', views.CommentViewSet, basename='comments')
# router.register(r'follow', views.FollowListCreateAPIView.as_view(), basename='follow')
# router.register(r'group', views.GroupListCreateAPIView.as_view(), basename='group')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/follow/', views.FollowListCreateAPIView.as_view(), name='follow'),
    path('v1/group/', views.GroupListCreateAPIView.as_view(), name='group'),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # TODO проверить тз на урл токена
]
