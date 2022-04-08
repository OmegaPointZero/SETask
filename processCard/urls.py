from django.urls import path
from .views import homePageView, getBatchID, verifyBatches

urlpatterns = [
    path("", homePageView, name="home"),
    path("batch", getBatchID, name="batch"),
    path("verify", verifyBatches, name="verify")
]