#Automating the creation of header responses with Puppet.
exec { 'command':
  command => 'apt-get -y update;
  apt-get -y install nginx;
  apt-get -y install haproxy;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  systemctl restart haproxy;
  service nginx restart',
  provider => shell,
}