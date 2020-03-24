# script that kill a killmenow process
exec { 'kill':
  command => '/usr/bin/pkill -f killmenow',
}
