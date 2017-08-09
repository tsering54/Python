urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^(?P<user_id>\d+)$', views.show),
]