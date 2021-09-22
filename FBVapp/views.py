from django.shortcuts import render
from .serializers import ProductSerializer  #responsible for qs-->dict or json-->dict
from .models import Product
from rest_framework.response import Response
from rest_framework import status

#for FBVs decorators are must
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#Non-ID based
@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def ProductListView(request):
    if request.method == 'GET':   # db--qs--dict--json--browser
        productList = Product.objects.all()
        serializer = ProductSerializer(productList,many=True)  #converted into dict
        return Response(serializer.data,status=status.HTTP_200_OK)    #fbv dont return status code but cbv does

    elif request.method == 'POST':  #brow-->json-->dict-->qs-->db
        serializer=ProductSerializer(data=request.data)    #this data is from brow
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    else:
        Response({'msg':'Only GET and POST method allowed'})

#Id
@api_view(['GET','PUT','DELETE'])
def ProductDetailView(request,pk):
    try:        # db--qs--dict--json--browser
        product = Product.objects.get(product_id=pk)
    except Product.DoesNotExist:
        return Response('Record does not exist',status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer=ProductSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method=='PUT':
            serializer = ProductSerializer(product,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            product.delete()
            return Response('Record deleted successfully',status=status.HTTP_204_NO_CONTENT)
