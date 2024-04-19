from django.contrib import admin
from django.urls import path,include

admin.site.site_title = "Nitin Gokarn Admin"

    # Text to put in each page's <div id="site-name">.
admin.site.site_header = "Nitin Gokarn Administration"

    # Text to put at the top of the admin index page.
admin.site.index_title = "Site administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
