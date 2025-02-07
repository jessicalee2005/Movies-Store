from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Cart, CartItem, Order

# View to display the shopping cart
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

# View to add a movie to the cart
@login_required
def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, movie=movie)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

# View to remove a movie from the cart
@login_required
def remove_from_cart(request, movie_id):
    cart = get_object_or_404(Cart, user=request.user)
    movie = get_object_or_404(Movie, id=movie_id)
    cart.cartitem_set.filter(movie=movie).delete()
    return redirect('cart_view')

# View to clear all items from the cart
@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.cartitem_set.all().delete()
    return redirect('cart_view')

# View to finalize purchase and create an order
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if cart.cartitem_set.exists():
        order = Order.objects.create(user=request.user, total_price=cart.total_price())
        order.movies.set(cart.movies.all())
        cart.cartitem_set.all().delete()
        return redirect('order_success')
    return redirect('cart_view')
