from django.shortcuts import render


def handler404(request, *args, **kwargs):
    response = render(request, '/workspace/catnip-cove/templates/catnip_cove/404.html', context = {})
    response.status_code = 404
    return response

def handler500(request, *args, **kwargs):
    response = render(request, '/workspace/catnip-cove/templates/catnip_cove/500.html', context={})
    response.status_code = 500
    return response