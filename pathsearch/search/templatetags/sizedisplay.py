from django import template

register = template.Library()

def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:
    
    
    """
    #value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = 'KB'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'MB'
    else:
        value = value / 1073741824.0
        ext = 'GB'
    return '%s %s' % (str(round(value, 2)), ext)

register.filter('sizify', sizify)

def datetime(value):
    value=value.split('T')
    date=value[0].split('-')
    hour=int(value[1].split('Z')[0].split(':')[0])
    min=value[1].split('Z')[0].split(':')[1]
    sec=value[1].split('Z')[0].split(':')[2]
    if hour >= 12:
        time='%s:%s %s'% (hour-12,min,'p.m')
    else:
        time='%s:%s %s'% (hour,min,'a.m')
    month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    datetime= '%s %s %s, %s' % (month[int(date[1])-1],date[2],date[0],time)
    return datetime



register.filter('sizify', sizify)
register.filter('datetime',datetime)
