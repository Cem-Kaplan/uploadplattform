from django.shortcuts import render, get_object_or_404
from .models import Video
from django.db.models import Q

def for_you_page(request):
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-uploaded_at')
    else:
        videos = Video.objects.all().order_by('-uploaded_at')
    
    return render(request, 'videos/for_you.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'videos/video_detail.html', {'video': video, 'videos' : videos})

def upload(request):
    return render(request, 'videos/upload.html')
