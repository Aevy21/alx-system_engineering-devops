# Puppet manifest to manage file limits for the holberton user

file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 4096\nholberton soft nofile 1024\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}
