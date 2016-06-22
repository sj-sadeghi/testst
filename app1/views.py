from django.shortcuts import render, HttpResponse
from .forms import Marks


def Grade(request):
    if request.method == "POST":
        print(request.POST)
        frc = Marks(request.POST)
        if frc.is_valid():
            frc.save()
            print(frc.__dict__)

            return render(request, 'result.html')
        else:
            return render(request, 'grade.html', context=locals())

    else:
        frc = Marks()
        return render(request, 'grade.html', context=locals())
