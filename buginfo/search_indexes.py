from haystack import indexes
from buginfo.models import BugInfo

class BugInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    info = indexes.CharField(model_attr='info')
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return BugInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(public=True)

