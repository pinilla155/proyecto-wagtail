from wagtail.admin.panels import FieldPanel, FieldRowPanel,InlinePanel, MultiFieldPanel,PageChooserPanel, StreamFieldPanel

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class PortfolioBlock(blocks.StructBlock):
    
    heading = blocks.CharBlock(classname="full title")
    image = ImageChooserBlock()
    intro = blocks.RichTextBlock()
   

    class Meta:
        template = 'batman/blocks/descripcion.html'
