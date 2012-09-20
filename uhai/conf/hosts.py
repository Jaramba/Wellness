from django_hosts import patterns, host

host_patterns = patterns('uhai',
    host(r'uhai', 'urls', name='default'),
)