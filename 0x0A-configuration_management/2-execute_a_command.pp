# execute a command in puppet
exec { 'killme':
        command => '/usr/bin/pkill -f killmenow',
}
