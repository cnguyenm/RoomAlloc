
from roomalloc.form.public import FeedbackForm

def feedback_form_context_processor(request):
    return {
        'feedback_form': FeedbackForm(),
        
    }