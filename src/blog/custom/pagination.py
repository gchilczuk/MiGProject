from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(data_to_paginate, page_nr, PPP=4):
    paginator = Paginator(data_to_paginate, PPP)
    try:
        posts = paginator.page(page_nr)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return posts