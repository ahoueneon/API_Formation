from rest_framework.views import APIView
from rest_framework.response import Response 


from shop.models import Category
from shop.serializers import CategorySerializer

from shop.models import Product
from shop.serializers import ProductSerializer

from shop.models import Article
from shop.serializers import ArticleSerializer 



class CategoryView(APIView):

    def get(self, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductView(APIView):
    def get(self, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ArticleView(APIView):
    def get(self, *args, **kwargs):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


        