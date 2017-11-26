
from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls import url, include
from errands.routers import HybridRouter
#from apertura_acuerdos.views.mail import email_one
router = HybridRouter()
from  publish.views import AuthorViewSet
#router.register(r'institucion', InstitucionViewSet,base_name=Institucion)
router.register(r'autor', AuthorViewSet, r"autor")


urlpatterns = [

    url(r'^', include(router.urls)),
   ]