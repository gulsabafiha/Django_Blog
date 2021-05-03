from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model= Post
    template_name= 'index.html'
    ordering=['-post_date']

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
def CategoryListView(request):
    cat_menu_list= Category.objects.all()
    return render(request,'categories_list.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    context= {'cats':cats.title().replace('-',' '),'category_posts':category_posts}
    return render(request,'categories.html',context)

class ArticleView(DetailView):
    model= Post
    template_name= 'article.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu=Category.objects.all()
        context = super(ArticleView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class= PostForm
    #fields = '__all__'
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    #form_class= PostForm
    fields = '__all__'
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model= Post
    form_class= EditForm
    template_name='update_post.html'
    #fields='__all__'
   

class DeletePostView(DeleteView):
    model= Post
    template_name='delete_post.html'
    fields='__all__'
    success_url= reverse_lazy('home')

class AddCommnetView(CreateView):
    model = Comment
    form_class= CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'

    def form_valid(self,form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)

