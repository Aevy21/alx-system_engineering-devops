# Puppet manifest to increase the maximum number of connections an Nginx server can handle

file { '/etc/default/nginx':
  ensure  => file,
  content => template('nginx/nginx_default.conf.erb'),
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/default/nginx'],
}
