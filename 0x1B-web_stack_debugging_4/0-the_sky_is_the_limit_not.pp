# Sky is the limit, let's bring that limit higher
exec { 'fix error':
      cwd     => '/etc/default/',
      command => 'sed -i "s/15/1000/" "nginx" && service nginx restart',
      path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}