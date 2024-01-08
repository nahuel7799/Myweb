from django.shortcuts import render, get_object_or_404
from .models import Blog, Page
from .forms import BlogForm, PageForm
from django.contrib.auth.decorators import login_required

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def search(request):
    # Implementar la lógica de búsqueda
    # ...
def about_me(request):
    # Implementar la vista de "Acerca de mí"
    # ...

def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'pages_list.html', {'pages': pages})

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'page_detail.html', {'page': page})

@login_required
def create_blog(request):
    # Implementar la vista para crear blogs
    # ...

@login_required
def edit_blog(request, blog_id):
    # Implementar la vista para editar blogs
    # ...

@login_required
def delete_blog(request, blog_id):
    # Implementar la vista para eliminar blogs
    # ...

# En myapp/views.py
def search(request):
    query = request.GET.get('q', '')
    results = Blog.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

# En myapp/views.py
def about_me(request):
    return render(request, 'about_me.html')

# En myapp/views.py
@login_required
def create_blog(request):
    # Implementar la lógica para crear blogs
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def edit_blog(request, blog_id):
    # Implementar la lógica para editar blogs
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    # Implementar la lógica para eliminar blogs
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete_blog.html', {'blog': blog})

# En myapp/views.py
@login_required
def create_blog(request):
    # Implementar la lógica para crear blogs
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def edit_blog(request, blog_id):
    # Implementar la lógica para editar blogs
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    # Implementar la lógica para eliminar blogs
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete_blog.html', {'blog': blog})

# En myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete_blog.html', {'blog': blog})

@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

@login_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

# En myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Blog

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    blogs = Blog.objects.all()
    return render(request, 'admin_dashboard.html', {'blogs': blogs})
