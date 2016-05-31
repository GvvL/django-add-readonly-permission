from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

class MyAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        salida = False
        if request.user.is_superuser:
            salida = True
        else:
            if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                salida = True
            else:
                if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                    salida = True
                else:
                    salida = False
        return salida

    def get_readonly_fields(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            return [el.name for el in self.model._meta.fields]

class MyTabularInline(admin.TabularInline):
    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        salida = False
        if request.user.is_superuser:
            salida = True
        else:
            if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                salida = True
            else:
                if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                    salida = True
                else:
                    salida = False
        return salida

def get_readonly_fields(self, request, obj=None):
    ct = ContentType.objects.get_for_model(self.model)
    if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
        return [el.name for el in self.model._meta.fields]


