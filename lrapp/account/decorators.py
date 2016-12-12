import functools

from .models import FavCategory, FavPage


def add_fav_to_dict(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        fc_list = fp_list = []
        if request.user.is_authenticated:
            fc_list = FavCategory.objects.get(user=request.user).categories.all()
            fp_list = FavPage.objects.get(user=request.user).pages.all()
        kwargs['fc_list'] = fc_list
        kwargs['fp_list'] = fp_list
        return view_func(request, *args, **kwargs)
    return wrapper
