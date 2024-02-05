# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep -f killmenow',
  unless      => '/usr/bin/pgrep -f killmenow && exit 1',
}
