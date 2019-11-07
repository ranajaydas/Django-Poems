from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Poem
from .forms import PoemForm


class PoemCreate(View):
    form_class = PoemForm
    template_name = 'poems/poem_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_poem = bound_form.save()
            return redirect(new_poem)
        else:
            return render(request, self.template_name, {'form': bound_form})


class PoemUpdate(View):
    form_class = PoemForm
    model = Poem
    template_name = 'poems/poem_form_update.html'

    def get_object(self, slug):
        return get_object_or_404(self.model, slug=slug)

    def get(self, request, slug):
        poem = self.get_object(slug)
        context = {
            'form': self.form_class(instance=poem),
            'poem': poem,
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        poem = self.get_object(slug)
        bound_form = self.form_class(request.POST, instance=poem)
        if bound_form.is_valid():
            new_poem = bound_form.save()
            return redirect(new_poem)
        else:
            context = {
                'form': bound_form,
                'poem': poem,
            }
            return render(request, self.template_name, context)


class PoemList(View):
    def get(self, request):
        poem_list = Poem.objects.all()
        return render(request, 'poems/poem_list.html', {'poem_list': poem_list})


class PoemDelete(View):
    def get(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        return render(request, 'poems/poem_confirm_delete.html', {'poem': poem})

    def post(self, request, slug):
        poem = get_object_or_404(Poem, slug__iexact=slug)
        poem.delete()
        return redirect('poem_list')


def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug__iexact=slug)
    return render(request, 'poems/poem_detail.html', {'poem': poem})
