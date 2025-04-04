from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserCreateView,
    UserDetailView,
    ReviewListView,
    ReviewDetailView,
    MovieReviewsView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/me/', UserDetailView.as_view(), name='user-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/movie/<str:title>/', MovieReviewsView.as_view(), name='movie-reviews'),
] 