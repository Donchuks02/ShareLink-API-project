from django.urls import path
from .views import ContentList, ContentDetail, UserList, UserDetail

urlpatterns = [
  path("users/", UserList.as_view()),
  path("users/<int:pk>/", UserDetail.as_view()),
  path("", ContentList.as_view(), name="content_list"),
  path("<int:pk>/", ContentDetail.as_view(), name="content_detail"),
]
