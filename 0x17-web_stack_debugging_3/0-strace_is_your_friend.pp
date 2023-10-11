exec { 'change_php_extension':
  command     => "sed -i '137s/\\.phpp/\\.php/' /var/www/html/wp-settings.php",
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
