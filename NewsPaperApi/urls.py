from django.contrib import admin
from django.urls import path
from NewsPaperApi.views import
urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookOnly.as_view())
]