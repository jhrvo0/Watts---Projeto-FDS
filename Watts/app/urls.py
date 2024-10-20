from django.urls import path
from .views import HomeViews, AddLocacao, DeleteLocacao, CriarComodo, DeleteComodo, CriarPontodeenergia, DeletePontodeenergia

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('addLocacao/', AddLocacao.as_view(), name='addLocacao'),
    path('deleteLocacao/<int:locacao_id>/', DeleteLocacao.as_view(), name='deleteLocacao'),
    path('addComodo/', CriarComodo.as_view(), name='addComodo'),
    path('deleteComodo/<int:comodo_id>/', DeleteComodo.as_view(), name='deleteComodo'),
    path('addPontodeenergia/', CriarPontodeenergia.as_view(), name='addPontodeenergia'),
    path('deletePontodeenergia/<int:pontodeenergia_id>/', DeletePontodeenergia.as_view(), name='deletePontodeenergia'),
]