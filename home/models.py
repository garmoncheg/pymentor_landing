from __future__ import absolute_import, unicode_literals
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet


class HomePage(Page):
    body = RichTextField(blank=True)
    team_description = models.ForeignKey(
        'home.TeamDescription',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    slogan = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('team_description'),
        FieldPanel('slogan')
    ]


@register_snippet
class ProjectSnippet(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class TeamMemberSnippet(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('text')
    ]

    def __str__(self):
        return self.title


@register_snippet
class ServiceSnippet(models.Model):
    icons = [
        'icon-laptop', 'icon-desktop', 'icon-tablet', 'icon-phone', 'icon-document', 'icon-documents', 'icon-search',
        'icon-clipboard', 'icon-newspaper', 'icon-notebook', 'icon-book-open', 'icon-browser', 'icon-calendar',
        'icon-presentation', 'icon-picture', 'icon-pictures', 'icon-video', 'icon-camera', 'icon-printer', 'icon-toolbox',
        'icon-briefcase', 'icon-wallet', 'icon-gift', 'icon-bargraph', 'icon-grid', 'icon-expand', 'icon-focus',
        'icon-edit', 'icon-adjustments', 'icon-ribbon', 'icon-hourglass', 'icon-lock', 'icon-megaphone', 'icon-shield',
        'icon-trophy', 'icon-flag', 'icon-map', 'icon-puzzle', 'icon-basket', 'icon-envelope', 'icon-streetsign',
        'icon-telescope', 'icon-gears', 'icon-key', 'icon-paperclip', 'icon-attachment', 'icon-pricetags',
        'icon-lightbulb', 'icon-layers', 'icon-pencil', 'icon-tools', 'icon-tools-2', 'icon-scissors', 'icon-paintbrush',
        'icon-magnifying-glass', 'icon-circle-compass', 'icon-linegraph', 'icon-mic', 'icon-strategy', 'icon-beaker',
        'icon-caution', 'icon-recycle', 'icon-anchor', 'icon-profile-male', 'icon-profile-female', 'icon-bike',
        'icon-wine', 'icon-hotairballoon', 'icon-globe', 'icon-genius', 'icon-map-pin', 'icon-dial', 'icon-chat',
        'icon-heart', 'icon-cloud', 'icon-upload', 'icon-download', 'icon-target', 'icon-hazardous', 'icon-piechart',
        'icon-speedometer', 'icon-global', 'icon-compass', 'icon-lifesaver', 'icon-clock', 'icon-aperture', 'icon-quote',
        'icon-scope', 'icon-alarmclock', 'icon-refresh', 'icon-happy', 'icon-sad', 'icon-facebook', 'icon-twitter',
        'icon-googleplus', 'icon-rss', 'icon-tumblr', 'icon-linkedin', 'icon-dribbble', 'icon-mobile'
    ]
    icon_choices = ((icon, icon) for icon in icons)

    title = models.CharField(max_length=255)
    text = RichTextField(blank=True)
    icon = models.CharField(max_length=50, choices=icon_choices)

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
        FieldPanel('icon')
    ]

    def __str__(self):
        return self.title


@register_snippet
class OfferSnippet(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.title


@register_snippet
class WhyChooseSnippet(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('text')
    ]

    def __str__(self):
        return self.title


@register_snippet
class TeamDescription(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('text')
    ]

    def __str__(self):
        return self.title

