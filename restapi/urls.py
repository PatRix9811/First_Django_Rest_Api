from django.urls import path, include

urlpatterns = [
    path('', include('booklist.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
