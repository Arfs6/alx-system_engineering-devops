# This manifest installs and configure an Nginx server.

# Install Nginx
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Configure html file
file { '/var/www/html/index.html':
  content => 'Hello World!\n',
}

# Configure server
exec {
}

# Start server
service { 'nginx':
  ensure => 'running',
  enable => 'true',
}
