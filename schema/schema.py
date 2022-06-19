
import graphene
from graphene_django import DjangoObjectType,DjangoListField
from blog.models import Blog, Project

class BlogQ(DjangoObjectType):
    class Meta:
        model=Blog
        fields=('id','title','tag','content','pic')
class ProjectQ(DjangoObjectType):
    class Meta:
        model=Project
        fields=('id','project_name','pic')
class Query(graphene.ObjectType):
    blog_list=graphene.List(BlogQ)
    node_blog=graphene.Field(BlogQ,id=graphene.Int())
    tag_recommend=graphene.List(BlogQ,Tag=graphene.String())
    projects=graphene.List(ProjectQ)
    def resolve_blog_list(root,info):
        return Blog.objects.all()
    def resolve_node_blog(root,info,id):
        print(root,info,id)
        return Blog.objects.get(pk=id)
    def resolve_tag_recommend(root,info,Tag):
        return Blog.objects.filter(tag=Tag)
    def resolve_projects(root,info):
        return Project.objects.all()
schema =graphene.Schema(query=Query)