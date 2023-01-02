from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NewsStory
from .forms import StoryForm



class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

    # ordering = ['-pub_date']

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# Add in import LoginRequiredMixIn to check user authentication first

# class StoryDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = NewsStory
#     success_url = reverse_lazy('news:index')

#     def get_queryset(self):
#         qs = super().get_queryset()
#         if not self.request.user.is_authenticated: - only need this for authentication
#             raise qs.model.DoesNotExist
#         qs = qs.filter(author=self.request.user)

#         return qs