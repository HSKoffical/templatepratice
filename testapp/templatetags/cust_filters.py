from django import template
register=template.Library()
def n_letter_msg(value,n):
    msg=value[:n].upper()
    return msg
register.filter('nlm',n_letter_msg)