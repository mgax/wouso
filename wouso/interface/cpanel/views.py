from django.contrib.auth.decorators import login_required
from django.http import Http404
from wouso.core.config.models import Setting
from wouso.interface import render_response
from wouso.utils.import_questions import import_from_file
from models import Customization

@login_required
def dashboard(request):
    customization = Customization()

    if request.method == "POST":
        for s in customization.props():
            val = request.POST.get(s.name, '')
            s.set_value(val)

    return render_response('cpanel/index.html', request, \
            {'settings': customization}
    )

@login_required
def importer(request):
    return render_response('cpanel/importer.html', request)

@login_required
def import_from_upload(request):
    import_from_file(request.FILES['file'], request.user)
    return render_response('cpanel/importer.html', request)