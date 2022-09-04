from django.core.management.base import BaseCommand
from imagesearch.models import Image
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'create image indexes for search engine'

    def handle(self, *args, **kwargs):
        images = Image.objects.all()
        list_path_image = [ img.image.path for img in images ]

        with open(os.path.join(settings.BASE_DIR, 'image_search_engine','write_path.txt'), 'w') as wl:
            for path in list_path_image:
                wl.write(str(path)+'\n')
        
        self.stdout.write(self.style.SUCCESS('image indexes create successfully'))
