from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import IdolForm, IdolTitleForm
from .models import IdolImage

def idol_home(request):
    idol_list = IdolImage.objects.order_by('title').all()

    paginator = Paginator(idol_list, 8) # 한 페이지에 8개씩 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    return render(request, 'moon/idol-home.html', context)

def upload(request):
    if request.method == 'POST':
        form = IdolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idol-home')
    else:
        form = IdolForm()
    return render(request, 'moon/upload.html', {'form': form})

def update(request, pk):
    idol = IdolImage.objects.get(pk=pk)
    if request.method == 'POST':
        form = IdolForm(request.POST, request.FILES, instance=idol)
        if form.is_valid():
            form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect('idol-detail', pk=idol.pk)
    else:
        form = IdolForm(instance=idol)
    return render(request, 'moon/update.html', {'form': form, 'idol': idol})

def detail(request, pk):
    idol = IdolImage.objects.get(pk=pk)
    if request.method == 'POST':
        form = IdolTitleForm(request.POST, instance=idol)
        if form.is_valid():
            form.save()
            return redirect('idol-detail', pk=idol.pk) # 수정 후 상세 페이지로 다시 리디렉션
    form = IdolTitleForm(instance=idol)
    return render(request, 'moon/detail.html', {'idol': idol, 'form': form})

def delete(request, pk):
    if request.method == 'POST':
        image = IdolImage.objects.get(pk=pk)
        image.delete()
        return redirect('idol-home')
    image = IdolImage.objects.get(pk=pk)
    return render(request, 'moon/delete.html', {'image': image})

def edit_title(request, pk):
    if request.method == 'POST':
        form = request.form.get('title')
        if form.is_valid():
            idol = IdolImage.objects.get(pk=pk)
            idol.title = form.cleaned_data['title']
            form.save()
            return redirect('idol-home')
    return render(request, 'moon/upload.html', {'form': form})