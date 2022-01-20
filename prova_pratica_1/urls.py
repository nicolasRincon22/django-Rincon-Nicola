from django.urls.conf import path

from .views import view_b
from .views import view_c


app_name="prova_pratica_1"

urlpatterns = [
    path("view_b",view_b,name="view_b"),
    path("view_c",view_c,name="view_c")
]