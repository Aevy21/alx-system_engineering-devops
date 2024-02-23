# Puppet manifest file: flask_install.pp

# Install Python 3.8.10
package { 'python3.8':
  ensure => latest,
}

# Install Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
