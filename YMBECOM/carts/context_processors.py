from .models import Cart,CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    #If 'admin' is not in the request.path, it proceeds to the else block.
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    # returns a dictionary with a single key-value pair, where the key is 'cart_count' and the value is the calculated cart_count variable.
    return dict(cart_count=cart_count)