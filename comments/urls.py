from django.urls import path
from .views import CommentsView, CommentsDetailView

urlpatterns = [
    path("/post/<id_post>/comments/", CommentsView.as_view()),
    path("/comments/<id_comment>/", CommentsDetailView.as_view()),
]
