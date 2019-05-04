from django.views.generic import View
from django.shortcuts import render
from image_gallery.settings import IMAGE_ROOT, IMAGE_URL
import os


class GalleryListView(View):
    def get(self, request):
        img_list = os.listdir(IMAGE_ROOT)
        img_url = IMAGE_URL

        params = {
            'images': img_list,
            'url': img_url
        }

        return render(request, 'list.html', params)
