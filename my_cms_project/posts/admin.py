from django.contrib import admin
from .models import Post, Category

# Personalizando a exibição da Categoria
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') # Campos exibidos na lista

# Personalizando a exibição do Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de posts
    list_display = ('title', 'author', 'status', 'created_at', 'category')
    
    # Filtros laterais
    list_filter = ('status', 'created_at', 'category', 'author')
    
    # Campos de pesquisa
    search_fields = ('title', 'content')
    
    # Preenchimento automático do slug
    prepopulated_fields = {'slug': ('title',)} 
    
    # Ordenação por data
    date_hierarchy = 'created_at'