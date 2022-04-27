from django.shortcuts import render
# from django.contrib import messages

from .forms import ReviewForm

def review(request):
    """ review view """
    review_form = ReviewForm()
    template = 'review/review.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)
