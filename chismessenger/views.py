from django.shortcuts import render, redirect
from .forms import AddChismisForm
from .models import Chismis


# Create your views here.
def home(request):
    if request.method == "POST":
        form = AddChismisForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
    else:
        form = AddChismisForm()

    all_chismis = Chismis.objects.all()
    context = {
        "form": form,
        "all_chismis": all_chismis,
    }

    return render(request, "home.html", context)
