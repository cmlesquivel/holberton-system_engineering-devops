exec { 'fix error':
      cwd     => '/var/www/html/',
      command => 'sed -i "s/false/true/g" "wp-config.php"',
      path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
