# Use exec resource to kill processes named "killmenow" if they exist
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
  path    => '/usr/bin',
}
