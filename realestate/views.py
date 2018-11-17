from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .filters import PostFilter

# Create your views here.
#list of posts made
def post_list(request):
    state = PostFilter(request.GET, queryset=Post.objects.all())
    
    return render(request, 'realestate/post_list.html', {'filter': state})
    
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'realestate/post_list.html', {'posts': posts})

#details of one post selected
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #primary key found and displays the one blog or 404 page displayed
    return render(request, 'realestate/post_detail.html', {'post': post})

#add a new post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit = False)    #don't save just yet, we need the info
            post.realtor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)  #redirects to the detailed page
    else:
        form = PostForm()
    return render(request, 'realestate/post_edit.html', {'form': form})

#edit currently existing post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit = False)
            post.realtor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'realestate/post_edit.html', {'form': form})

#delete a post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    
def add_message(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('Thank_you')
    else:
        form = CommentForm()
    return render(request, 'realestate/add_message.html', {'form': form})

def Thank_you(request):
    return render(request, 'realestate/Thank_you.html')

#trying to filter
def product_state(request):
    state = PostFilter(request.GET, queryset=Post.objects.all())
    
    return render(request, 'realestate/product_list.html', {'filter': state})
    
        
    
            
