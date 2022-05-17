from django.shortcuts import render, get_object_or_404, redirect
from .models import Celebrity
from .models import Post
from .models import Comment
from .models import NewCelebrity
from django.utils import timezone


def index(request):
    return render(request, 'pybo/mainview.html')

def celebrities(request):
    celebrity_list = Celebrity.objects.all()
    context = {'celebrity_list': celebrity_list}
    return render(request, 'pybo/celebrities.html', context)

def post(request, celebrity_name):
    celebrity = Celebrity.objects.get(name = celebrity_name)
    post_list = Post.objects.filter(celebrity=celebrity)
    context = {'post_list': post_list, 'celebrity' : celebrity}
    return render(request, 'pybo/post.html', context)

def detail(request, celebrity_name, post_id):
    post = Post.objects.get(id = post_id)
    celebrity = Celebrity.objects.get(name = celebrity_name)
    comment_list = Comment.objects.filter(post = post)
    context = {'comment_list': comment_list, 'post': post, 'celebrity' : celebrity}
    return render(request, 'pybo/detail.html', context)

def comment_create(request, celebrity_name, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, content=request.POST.get('content'), create_date=timezone.now())
    comment.save()
    return redirect('pybo:detail', celebrity_name=celebrity_name, post_id=post.id)

def post_create(request, celebrity_name):
    celebrity = get_object_or_404(Celebrity, name=celebrity_name)
    post = Post(celebrity=celebrity, subject=request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now())
    post.save()
    return redirect('pybo:detail', celebrity_name=celebrity_name, post_id=post.id)

def newcel(request):
    newcelebrity_list = NewCelebrity.objects.all()
    context = {'newcelebrity_list': newcelebrity_list}
    return render(request, 'pybo/newcel.html', context)

def newpost(request, celebrity_name):
    context = {'celebrity_name' : celebrity_name}
    return render(request, 'pybo/newpost.html', context)

def celebrity_create(request):
    newcelebrity = NewCelebrity(name=request.POST.get('name'))
    newcelebrity.save()
    return redirect('pybo:newcel')