from .models import POST
from haystack import indexes

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(use_template=True, document=True)
    title = indexes.CharField(model_attr='title')
    def get_model(self):
        return POST
    def index_queryset(self, using=None):
        return self.get_model().objects.all()