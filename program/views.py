# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Program

# Create your views here.
# def index(request):
#     programs = Program.objects.all().order_by("-pk")
#
#     return render(request, "program/program_list.html", {"programs": programs})
# def single_program_page(request, pk):
#     program = Program.objects.get(pk=pk)
#
#     return render(request, "program/program_detail.html", {"program": program})
class ProgramList(ListView):
    model = Program
    ordering = "-pk"
class ProgramDetail(DetailView):
    model = Program