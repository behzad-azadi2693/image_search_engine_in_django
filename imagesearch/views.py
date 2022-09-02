from rest_framework.decorators import api_view, permission_classes
from image_search_engine.colordescriptor import ColorDescriptor
from .serializers import ImageListSerializer, ImageSerializer
from django.views.decorators.csrf import csrf_exempt
from image_search_engine.searcher import Searcher
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Case, When
from django.conf import settings
from .models import Image
from uuid import uuid4
import argparse
import cv2
import os


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def image_search(request):

    if request.method == 'GET':
        serializer = ImageSerializer().data
        
        return Response(serializer, status=200)

    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        
        if serializer.is_valid():
            img = serializer.initial_data['image']

            pre, form = str(img).split('.')
            new_name  = f"{pre}-{uuid4()}.{form}"

            user_data_path = os.path.join(settings.BASE_DIR, 'image_search_engine', 'user_data', str(new_name))

            with open(user_data_path, 'wb') as udp:
                image = img.read()
                udp.write(image)

            cd = ColorDescriptor((8, 12, 3))

            query = cv2.imread(f'{user_data_path}')
            features = cd.describe(query)

            indexPath = os.path.join(settings.BASE_DIR, 'image_search_engine', 'image_index.csv')

            searcher = Searcher(indexPath)
            similiar_image = searcher.search(features)

            image_name_list = [rst[1].split('/')[1] for rst in similiar_image]

            preserved = Case(*[When(image=field, then=position) for position, field in enumerate(image_name_list)])
            results = Image.objects.filter(image__in = image_name_list).order_by(preserved)
            
            srz = ImageListSerializer(results, many=True)

            return Response(srz.data, status=200)
