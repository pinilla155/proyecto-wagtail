from django.db import models

from wagtail.fields import StreamField
from wagtail.models import Collection, Page, Site, SiteManager, SiteRootPath
from wagtail.fields import RichTextField

from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from modelcluster.fields import ParentalKey
from batman.blocks import PortfolioBlock





class InicioFormField(AbstractFormField):
    page = ParentalKey('InicioPage', related_name='form_fields')

class InicioPage(AbstractForm, Page):
    subtitle = models.CharField(max_length=100, blank=True)
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    inicio = StreamField([
        ('inicio', PortfolioBlock()),
    ], null=True, blank=True)

    about_text = RichTextField(blank=True)
    about_CTA_text = models.CharField(max_length=100, blank=True)
    about_CTA_link = models.URLField(blank=True)

    content_panels = AbstractForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('subtitle'),
            FieldPanel('profile_image'),
        ], "Hero"),

        FieldPanel('inicio'),

        MultiFieldPanel([
            FieldPanel('about_text', classname="full"),
            FieldPanel('about_CTA_text'),
            FieldPanel('about_CTA_link'),
        ], "Hero"),

        InlinePanel('form_fields', label="Form fields"),
    ]


