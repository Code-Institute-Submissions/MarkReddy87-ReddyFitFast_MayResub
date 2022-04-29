""" Add relevant imports below """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """ A view to show all reviews """
    reviews = Review.objects.all()
    context = {
       'reviews': reviews,
    }

    return render(request, 'review/reviews.html', context)


def review_detail(request, review_id):
    """ A view to show individual review details """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, 'review/review_detail.html', context)


def add_review(request):
    """ review view """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            user = request.user
            review.posted_by = user
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('review'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'review/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_review(request, review_id):
    """ Edit a review on the site """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'review/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)

def delete_review(request, review_id):
    """ Delete a review from the site """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('review'))
