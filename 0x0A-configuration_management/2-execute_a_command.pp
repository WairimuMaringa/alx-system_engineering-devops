# Create a manifest that kills a process called killmenow using Puppet

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
