from django.shortcuts import render, get_object_or_404

from notes.models import Category


def home(request):
    return render(request, 'index.html', {'categories': Category.objects.all()})

def category_detail(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'detail.html', {'category': category})


