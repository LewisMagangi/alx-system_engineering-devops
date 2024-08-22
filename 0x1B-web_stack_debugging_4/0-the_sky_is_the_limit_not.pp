# Increasing the amount of traffic depending on the Nginx Web Server Strength..

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restarting Nginx Webserver
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
