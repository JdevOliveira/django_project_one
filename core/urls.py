from django1.urls import path

from .views import index, contato, smash, produto


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('smash', smash, name='smash'),
    path('produto/<int:pk>', produto, name='produto'),
]
