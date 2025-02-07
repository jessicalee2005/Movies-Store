from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Order
from .forms import ReviewForm, OrderForm

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': template_data})

def show(request, id):
    movie = get_object_or_404(Movie, id=id)
    reviews = Review.objects.filter(movie=movie)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movies/show.html', {'template_data': template_data})

@login_required
def add_review(request, movie_id): #aashvi changes start
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movies.show', id=movie.id)  # Redirect to movie page

    else:
        form = ReviewForm()

    return render(request, 'movies/add_review.html', {'form': form, 'movie': movie})


@login_required
def place_order(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.movie = movie
            order.user = request.user  # Link the order to the logged-in user
            order.save()
            return redirect('movies.show', id=movie.id)

    else:
        form = OrderForm()

    return render(request, 'movies/place_order.html', {'form': form, 'movie': movie})


@login_required
def update_review(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movies.show', id=review.movie.id)  # redirect
    else:
        form = ReviewForm(instance=review)

    return render(request, 'movies/add_review.html', {'form': form, 'movie': review.movie})

@login_required
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    movie_id = review.movie.id
    review.delete()  # Delete the review
    return redirect('movies.show', id=movie_id)  # redirect to movie page

@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('movies.show', id=order.movie.id)  # redirect
    else:
        form = OrderForm(instance=order)

    return render(request, 'movies/place_order.html', {'form': form, 'movie': order.movie})

@login_required
def delete_order(request, id): #aashvi changes end
    order = get_object_or_404(Order, id=id)
    movie_id = order.movie.id
    order.delete()  # Delete the order
    return redirect('movies.show', id=movie_id)  # redirect