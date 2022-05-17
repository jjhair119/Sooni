from django.contrib import admin
from .models import Celebrity
from .models import Post
from .models import Comment
from .models import NewCelebrity

admin.site.register(Celebrity)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(NewCelebrity)