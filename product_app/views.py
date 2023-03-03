from django.http import JsonResponse
from rest_framework.views import APIView

from product_app.models import Product, Category, Manufacturer
from product_app.serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer


class ProductAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = ProductSerializer(Product.objects.all(), many=True)
        else:
            try:
                serializer = ProductSerializer(Product.objects.get(pk=pk))
            except Product.DoesNotExist:
                return JsonResponse({'Products': 'products not found'})
        return JsonResponse({'Products': serializer.data})

    def post(self, request, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'Product': serializer.data}, status=201)

    def patch(self, request, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['pk'])
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'})

        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse({'Product': serializer.data}, status=201)

    def delete(self, request, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['pk'])
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'})

        product.delete()

        return JsonResponse({'message': "Product was deleted"})


class CategoryAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = CategorySerializer(Category.objects.all(), many=True)
        else:
            try:
                serializer = CategorySerializer(Category.objects.get(pk=pk))
            except Category.DoesNotExist:
                return JsonResponse({'Categories': 'categories not found'})
        return JsonResponse({'Categories': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    def patch(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'})

        serializer = CategorySerializer(data=request.data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'})

        product.delete()

        return JsonResponse({'message': "Category was deleted"})


class ManufacturerAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            serializer = ManufacturerSerializer(Manufacturer.objects.all(), many=True)
        else:
            try:
                serializer = ManufacturerSerializer(Manufacturer.objects.get(pk=pk))
            except Manufacturer.DoesNotExist:
                return JsonResponse({'Manufacturers': 'Manufacturers not found'})
        return JsonResponse({'Manufacturers': serializer.data})

    def post(self, request, **kwargs):
        serializer = ManufacturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'Manufacturer': serializer.data}, status=201)

    def patch(self, request, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['pk'])
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Manufacturer not found'})

        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse({'Manufacturer': serializer.data}, status=201)

    def delete(self, request, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['pk'])
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Manufacturer not found'})

        product.delete()

        return JsonResponse({'message': "Manufacturer was deleted"})