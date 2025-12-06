from django import forms
from .models import Post

# ModelForm para criação de posts
class PostForm(forms.ModelForm):
    
    # Sobrescreve o campo de status para esconder a opção 'published' 
    # e garantir que novos posts comecem como 'draft' por padrão.
    status = forms.CharField(
        widget=forms.HiddenInput(),
        initial='draft'
    )
    
    class Meta:
        model = Post
        # Define os campos que o usuário poderá preencher no formulário
        fields = ('title', 'content', 'category', 'status')
        
        # Opcional: Personalizar labels
        labels = {
            'title': 'Título do Artigo',
            'content': 'Conteúdo Completo',
            'category': 'Categoria',
        }
        
        # Opcional: Adicionar classes CSS ou atributos HTML
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }