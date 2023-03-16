from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.forms.panels import FormSubmissionsPanel

from .models import InicioPage, InicioFormField


class InicioFormFieldAdmin(ModelAdmin):
    model = InicioFormField
    menu_label = 'Form Fields'
    menu_icon = 'list-ul'
    list_display = ('label', 'field_type', 'required')


class InicioPageAdmin(ModelAdmin):
    model = InicioPage
    menu_label = 'Inicio Pages'
    menu_icon = 'home'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'subtitle', 'live', 'has_unpublished_changes')
    list_filter = ('live', 'has_unpublished_changes', 'first_published_at')
    search_fields = ('title', 'subtitle')

    # Define panels for Page edit view
    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('subtitle'),
        FieldPanel('profile_image'),
        FieldPanel('inicio'),
        FieldPanel('about_text', classname="full"),
        FieldPanel('about_CTA_text'),
        FieldPanel('about_CTA_link'),
        InlinePanel('form_fields', label="Form fields"),
        FormSubmissionsPanel(),
    ]


# Register the InicioPageAdmin and InicioFormFieldAdmin with the Wagtail admin
modeladmin_register(InicioPageAdmin)
modeladmin_register(InicioFormFieldAdmin)
