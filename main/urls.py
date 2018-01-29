from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_registration_app.urls')),
    url(r'^books/', include('apps.book_app.urls')),
    url(r'^reviews/', include('apps.review_app.urls')),
]
