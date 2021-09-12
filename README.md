<p align="center">
  <img width="250"
       src="https://github.com/addy3494/jc/raw/master/assets/logo.png">
<h1 align="center">Jc - A Lazy SSH Command Line Helper</h1>

![](https://img.shields.io/badge/license-MIT-green.svg?style=flat)

<img
  src="https://github.com/addy3494/jc/raw/master/assets/demo.gif"
  alt="Jc - A Lazy SSH Command Line Helper"
  width="100%"
  align="center"
/>

*Manage your infrastructure, Never loose/forget passwords again.*


## Key Features:
- One time setup, Initialize a local database to store all your infrastructure infomation
- Supports all Linux, Unix, MacOS systems as authentication is via ssh

Connection is prioritzed by
  1. ssh-key
  2. ssh-pass
## Requirements
- python3
- [fzf](https://github.com/junegunn/fzf)
- ssh

## Configure
```
  git clone https://github.com/addy3494/jc.git
  pip install -r requirements.txt
  python3 /path/t0/jc
```
## Contributing
Bug reports and pull requests are welcome on GitHub at [jc]( https://github.com/addy3494/jc ) repository.

This project is intended to be a safe, welcoming space for collaboration and contributors are expected to adhere to the
[Contributor Covenant](http://contributor-covenant.org) code of conduct.

  1. Fork it ( https://github.com/addy3494/jc )
  1. Create your feature branch (`git checkout -b my-new-feature`)
  1. Commit your changes (`git commit -am 'Add some feature'`)
  1. Push to the branch (`git push origin my-new-feature`)
  1. Create a new Pull Request

## Author
* **gh0s1** - *Owner* - [gh0s1]( https://github.com/addy3494 )

## Disclaimer

This project
* Has been created to tackle my personal use-case.
* Wont take any responsibility of any damage-dealt / Passwords leaks. It is assumed you are using this package in a controlled environment.
* Is not production ready / safe
* Is intended only for personal use
* Is Just a wrapper *(quality-of-life improvements)* of the existing details which you already have
* Assumes you already have available connection for key-based auth, this wont create / establish any
## Credits

  This project makes use
  * [pyfzf](https://github.com/nk412/pyfzf)
  * [fzf](https://github.com/junegunn/fzf)

The project is available as open source under the terms of the [MIT License](LICENSE)
