# Use exec resource to kill processes named "killmenow" if they exist
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
