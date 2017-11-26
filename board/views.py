from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Entregas
from .forms import EntregasForm, CommentForm, DocumentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def entregas_list(request):
    entregas = Entregas.objects.filter(published_date__lte=timezone.now()).order_by('fecha_entrega')
    return render(request, 'board/entregas_list.html', {'entregas': entregas})
	
def entrega_detail(request, pk):
    entrega = get_object_or_404(Entregas, pk=pk)
    return render(request, 'board/entrega_detail.html', {'entrega': entrega})
	
	
def entrega_new(request):
    if request.method == "POST":
        form = EntregasForm(request.POST)
        if form.is_valid():
            entrega = form.save(commit=False)
            entrega.author = request.user
       
            entrega.save()
            return redirect('entrega_detail', pk=entrega.pk)
    else:
        form = EntregasForm()
    return render(request, 'board/entrega_edit.html', {'form': form})
	
def entrega_edit(request, pk):
    entrega = get_object_or_404(Entregas, pk=pk)
    if request.method == "POST":
        form = EntregasForm(request.POST, instance=entrega)
        if form.is_valid():
            entrega = form.save(commit=False)
            entrega.author = request.user
            entrega.published_date = timezone.now()
            entrega.save()
            return redirect('entrega_detail', pk=entrega.pk)
    else:
        form = EntregasForm(instance=entrega)
    return render(request, 'board/entrega_edit.html', {'form': form})
	
def entrega_remove(request, pk):
    entrega = get_object_or_404(Entregas, pk=pk)
    entrega.delete()
    return redirect('entregas_list')
	
def add_comment_to_entrega(request, pk):
    entrega = get_object_or_404(Entregas, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entrega = entrega
            comment.save()
            return redirect('entrega_detail', pk=entrega.pk)
    else:
        form = CommentForm()
    return render(request, 'board/add_comment_to_entrega.html', {'form': form})
	
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entregas_list')
    else:
        form = DocumentForm()
    return render(request, 'board/model_form_upload.html', {
        'form': form
    })