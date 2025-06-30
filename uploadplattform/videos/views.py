from django.shortcuts import render, get_object_or_404
from .models import Video

def for_you_page(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/for_you.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'videos/video_detail.html', {'video': video})

def upload(request):
    return render(request, 'videos/upload.html')