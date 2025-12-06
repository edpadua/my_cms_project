
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,  # <-- ESTA PODE ESTAR FALTANDO
    PostDeleteView   # <-- E ESTA TAMBÉM
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    
    # Rota de EDIÇÃO
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'), 
    
    # Rota de EXCLUSÃO (NOVA ROTA)
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Rota de DETALHE (Genérica, continua por último)
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]