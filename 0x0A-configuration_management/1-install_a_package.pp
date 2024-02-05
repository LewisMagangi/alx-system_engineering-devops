# A puppet manifest to install flask from pip3

package { 'flask':
  ensure  =>  installed,
  provider  => 'pip3'
}
