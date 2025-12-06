from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, # Importe UpdateView
    DeleteView  # Importe DeleteView (para o próximo passo)
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin # Importe este Mixin para checar permissão
)
from .models import Post
from .forms import PostForm

# View para listar posts na página inicial (mantida)
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(status='published')

# View para exibir um único post (NOVA CLASSE)
class PostDetailView(DetailView):
    # 1. Qual Modelo deve ser usado?
    model = Post
    
    # 2. Qual template deve ser renderizado?
    template_name = 'posts/post_detail.html'
    
    # 3. O Django por padrão usa 'pk' (primary key/id). 
    #    Estamos definindo para usar o 'slug' na URL.
    slug_field = 'slug' 
    
    # 4. Nome da variável no template (opcional, mas claro)
    context_object_name = 'post' 

    # 5. Sobrescreve a consulta para garantir que apenas posts publicados sejam acessíveis
    def get_queryset(self):
        # Garante que só posts 'published' sejam exibidos
        return Post.objects.filter(status='published')

    # View para criar um novo post
class PostCreateView(LoginRequiredMixin, CreateView):
    # Garante que apenas usuários logados possam acessar esta página
    # Se não estiver logado, redireciona para a página de login
    
    model = Post
    form_class = PostForm # Usa o formulário que criamos
    template_name = 'posts/post_create.html'
    
    # Define para onde redirecionar após o post ser criado com sucesso
    # 'post_list' é o nome da nossa rota principal
    success_url = reverse_lazy('post_list') 

    # Sobrescreve o método para atribuir o autor antes de salvar
    def form_valid(self, form):
        # 1. Atribui o usuário logado atualmente como o autor do post
        form.instance.author = self.request.user
        
        # 2. Continua o processo de salvamento
        return super().form_valid(form)


    # View para editar um post existente
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm 
    template_name = 'posts/post_edit.html' 
    slug_url_kwarg = 'slug' # Usa o slug da URL para buscar
    context_object_name = 'post'

    # 1. Checa se o usuário é o autor do post
    def test_func(self):
        post = self.get_object() # Obtém o post atual
        return self.request.user == post.author # Retorna True se o usuário logado for o autor

    # 2. Define o redirecionamento após a edição
    def get_success_url(self):
        # Redireciona de volta para a página de detalhes do post editado
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


# View para excluir um post existente
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html' # Template de confirmação
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    # Define para onde redirecionar após a exclusão ser concluída
    success_url = reverse_lazy('post_list') 

    # Checa se o usuário é o autor do post (Mesma checagem que a edição)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author