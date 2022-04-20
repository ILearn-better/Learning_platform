from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"deepLearning",views.deepLearning),
    # url(r"^pr1",views.pr1),
    url(r"upload_file",views.upload_file),
]