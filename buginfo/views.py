from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render_to_response
from models import BugInfo
from haystack.forms import SearchForm
# Create your views here.
class BugDetailView(DetailView):
   model = BugInfo
   template_name = 'search/detail.html'
   queryset = BugInfo.objects.all()
   context_object_name = 'bug'
   def get(self, request, *args, **kwargs):
       id = self.kwargs.get('pk')
       self.object = self.queryset.get(id=id)
       context = self.get_context_data(object=self.object)
       return self.render_to_response(context)


def Search(request):
    form = SearchForm(request.GET)
    results = form.search()
    return render_to_response('search/search.html', {'results': results})
