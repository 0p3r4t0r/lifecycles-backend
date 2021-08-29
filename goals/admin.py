from goals.models import OneOff, OverInterval
from django.contrib import admin
from django.forms.models import ModelForm


class GoalAdmin(admin.ModelAdmin):
    readonly_fields = ('user', )
    exclude = ( 'completed_at', )
    form = ModelForm
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(OneOff)
class OneOffAdmin(GoalAdmin):
    pass


@admin.register(OverInterval)
class OverIntervalAdmin(GoalAdmin):
    pass
