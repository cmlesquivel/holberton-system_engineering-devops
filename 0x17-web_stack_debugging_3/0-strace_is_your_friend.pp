# fix Strace is your friend
exec { 'fix error':
      cwd     => '/var/www/html/',
      command => 'sed -i "s/false/true/g" "wp-config.php" && sed -i "s/phpp/php/g" "wp-settings.php"',
      path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
