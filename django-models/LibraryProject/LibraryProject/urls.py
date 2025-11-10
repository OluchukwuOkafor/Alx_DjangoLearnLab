from django.contrib import admin
from django.urls import path, include  # include function to add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # route to your app
]
