#Client configuration file with Puppet
include stdlib

file_line {
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line {
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
