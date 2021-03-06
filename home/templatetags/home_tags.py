from django import template
from home.models import TeamMemberSnippet, ServiceSnippet, OfferSnippet

register = template.Library()


@register.inclusion_tag('home/tags/team_members.html', takes_context=True)
def team_members(context):
    return {
        'team_members': TeamMemberSnippet.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/services.html', takes_context=True)
def services(context):
    return {
        'services': ServiceSnippet.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/offers.html', takes_context=True)
def offers(context):
    return {
        'offers': OfferSnippet.objects.all(),
        'request': context['request']
    }
