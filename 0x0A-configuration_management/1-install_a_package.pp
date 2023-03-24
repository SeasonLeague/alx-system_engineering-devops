#Puppet to install a program 

package { 'flask':
  ensure    => '2.1.0',
  provider  => 'pip3',
}

