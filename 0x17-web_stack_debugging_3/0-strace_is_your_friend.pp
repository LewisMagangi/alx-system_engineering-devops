# A puppet script to fix an Apache server returning a 500 status error code

exec { 'fix error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
