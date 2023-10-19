# Fix server.

exec { 'sed-edit-config':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => "/usr/local/bin/:/bin"
}
exec { 'sudo-restart-nginx':
  command => "/etc/init.d/nginx restart",
  path    => "/usr/bin/:/bin/:/usr/local/bin/"
}
