from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('', include('cursos.urls')),
    # path('capacitacao-profissional/palestras/', include(('palestras.urls', 'palestras'), namespace ='palestras')),

    path('servicos/cevest/', include('cevest_os.urls')),
    path('cevest/almoxarifado/', include('cevest_almoxarifado.urls')),
    path('estagio/', include('estagio.urls')),

    path('administracao/', include('administracao.urls')),    
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
