from django.shortcuts import render, redirect, reverse
from .forms import UserForm


def index(request):
    form = UserForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect(reverse('Randomize:submit'))

    return render(request, 'index.html', {'form': form})


def submit(request):
    return render(request, 'finish.html')