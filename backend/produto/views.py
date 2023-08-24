from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import JsonResponse
from produto.models import Produto

# Create your views here.

class ProdutoNovo(generic.CreateView):
    model = Produto
    fields = '__all__'

class ProdutoDetalhe(generic.DetailView):
    model = Produto
    
class ProdutoLista(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()

class ProdutoAtualizar(generic.UpdateView):
    model = Produto
    fields = ['nome', 'preco', ]
    template_name_suffix = '_update_form'
    
class ProdutoApagar(generic.DeleteView):
    model = Produto
    success_url = reverse_lazy('produto-lista')
    
class ProdutoJSONView(View):
    def get (self, *args, **kwargs):
        produtos = Produto.objects.all()
        data = [
            {
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
                'estoque': produto.estoque
            } 
            
            for produto in produtos
        ] 
        
        return JsonResponse(data, safe=False)