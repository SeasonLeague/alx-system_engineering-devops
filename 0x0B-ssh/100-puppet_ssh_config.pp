# Sets up client-side SSH config
# to allow login w/o passord.

include stdlib
file_line {'Declarative identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true
}

file_line {'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true
}
