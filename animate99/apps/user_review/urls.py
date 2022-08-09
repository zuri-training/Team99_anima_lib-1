from django.urls import path
from .views import LibraryListView,usageExamples, likes, IsFavoriteView, SettingsView
urlpatterns = [
     path("library", LibraryListView.as_view(), name='library' ),
     path("settings/<int:pk>/", SettingsView.as_view(), name='settings'),
     path("usageexamples", usageExamples, name='usageexamples' ),
     path("likes", likes, name='likes' ),
     path("isfavourite/<int:pk>/", IsFavoriteView.as_view(), name='favourite')
]
