from warnings import catch_warnings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Celebrity
from .models import Post
from .models import Comment
from .models import NewCelebrity
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.contrib import messages


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

@login_required(login_url='common:login')
def comment_create(request, celebrity_name, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, content=request.POST.get('content'), create_date=timezone.now())
    comment.author = request.user
    comment.save()
    return redirect('pybo:detail', celebrity_name=celebrity_name, post_id=post.id)

@login_required(login_url='common:login')
def post_create(request, celebrity_name):
    celebrity = get_object_or_404(Celebrity, name=celebrity_name)
    post = Post(celebrity=celebrity, subject=request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now())
    post.author = request.user
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
    try :
        NewCelebrity.objects.get(name=request.POST.get('name'))
        messages.warning(request, "이미 요청된 연예인입니다.")
    except :
        newcelebrity = NewCelebrity(name=request.POST.get('name'))
        newcelebrity.save()
    return redirect('pybo:newcel')

def celebrityList_create(request):
    try :
        Celebrity.objects.get(name=request.POST.get('name'))
    except :
        celebrity = Celebrity(name=request.POST.get('name'))
        celebrity.save()
    delcelname = request.POST.get('name')
    try:
        delcel = NewCelebrity.objects.get(name=delcelname)
    except MultipleObjectsReturned:
        delcel = NewCelebrity.objects.filter(name=delcelname).first()
    delcel.delete()
    return redirect('pybo:newcel')

def celebrityList_del(request):
    delcelname = request.POST.get('name')
    try:
        delcel = NewCelebrity.objects.get(name=delcelname)
    except MultipleObjectsReturned:
        delcel = NewCelebrity.objects.filter(name=delcelname).first()
    delcel.delete()
    return redirect('pybo:newcel')

def manager(request):
    celebrity_list = Celebrity.objects.all()
    context = {'celebrity_list': celebrity_list}
    return render(request, 'pybo/manager.html', context)

def celebrity_del(request):
    delcelname = request.POST.get('name')
    delcel = Celebrity.objects.filter(name=delcelname)
    delcel.delete()
    return redirect('pybo:manager')

def celebrityList_createM(request):
    try :
        Celebrity.objects.get(name=request.POST.get('name'))
        messages.warning(request, "이미 등록된 연예인입니다.")
    except :
        celebrity = Celebrity(name=request.POST.get('name'))
        celebrity.save()
    return redirect('pybo:manager')