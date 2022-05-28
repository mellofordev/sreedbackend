from dataclasses import field
import graphene
from graphene_django import DjangoObjectType
from blog.models import Blog

class BlogQ(DjangoObjectType):
    class Meta:
        model=Blog
        fields=('id','title','tag','content')
class Query(graphene.ObjectType):
    blog_list=graphene.List(BlogQ)

    def resolve_blog_list(root,info):
        return Blog.objects.all()

schema =graphene.Schema(query=Query)