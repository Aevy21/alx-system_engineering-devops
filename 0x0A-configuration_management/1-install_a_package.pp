# Install Flask using pip3

# Description:
# This Puppet manifest ensures that Flask version 2.1.0 is installed using pip3, the package manager for Python 3.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
