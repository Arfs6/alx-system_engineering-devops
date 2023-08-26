# create a config file for ssh
#
$home = $facts['home']
file { '/root/.ssh/config':
  ensure  => 'file',
  path    => "/root/.ssh/config",
  mode    => '0600',
  content => "\
host 54.237.208.82
	PasswordAuthentication = no
	IdentityFile = ~/.ssh/school
	${home}/.ssh/config
"
}
