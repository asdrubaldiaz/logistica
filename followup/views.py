from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cases
from board.models import Barcos
from .forms import CasesForm
from django.shortcuts import redirect

# Create your views here.

	
def case_list(request):
    cases = Cases.objects.all()
    return render(request, 'followup/follow_list.html', {'cases': cases})
	
def case_detail(request, pk):
    case = get_object_or_404(Cases, pk=pk)
    return render(request, 'followup/case_detail.html', {'case': case})
	
	
def case_new(request):
    if request.method == "POST":
        form = CasesForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.author = request.user
            case.published_date = timezone.now()
            case.save()
            return redirect('case_detail', pk=case.pk)
    else:
        form = CasesForm()
    return render(request, 'followup/case_edit.html', {'form': form})
	
