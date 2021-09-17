<p align="center">
  <img width="250"
       src="https://github.com/addy3494/jc/raw/master/assets/logo.png">
<h1 align="center">Jc - A Lazy SSH Command Line Helper</h1>

![](https://img.shields.io/badge/license-MIT-green.svg?style=flat)
<a href="https://www.buymeacoffee.com/addy3494" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 130px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<img
  src="https://github.com/addy3494/jc/raw/master/assets/demo.gif"
  alt="Jc - A Lazy SSH Command Line Helper"
  width="100%"
  align="center"
/>

*Manage your infrastructure, Never loose/forget passwords again.*

***
## Key Features:
- One time setup, Initialize a local database to store all your infrastructure infomation
- Supports all Linux, Unix, MacOS systems as authentication is via ssh

Connection is prioritzed by
  1. ssh-key
  2. ssh-pass
***
## Requirements
- python3
- [fzf](https://github.com/junegunn/fzf)
- ssh
***
## Configure
* VIA GIT
  ```
    git clone https://github.com/addy3494/jc.git && cd jc
    pip install -r requirements.txt
    python3 /path/to/jc
  ```
* VIA PIP
  ```
    pip install justconnect
    python3 -m jc
  ```
* MANUAL INSTALL
  ```
    git clone https://github.com/addy3494/jc.git && cd jc
    python3 setup.py install
    python3 -m jc
  ```
***
## Disclaimer

### This repository,
* Is Created to tackle my personal use-case.
* Is not production ready/safe.
* Is just a wrapper *(quality-of-life improvements)* of the existing details which you already have.
* Assumes you already have available connection for key-based auth and will not create/establish any.
* Will not take any responsibility of damage-dealt/passwords-leaks etc. It is assumed you are using this package in a controlled environment.

***
## Contributing
Bug reports and pull requests are welcome on GitHub at [jc]( https://github.com/addy3494/jc ) repository.

This project is intended to be a safe, welcoming space for collaboration and contributors are expected to adhere to the
[Contributor Covenant](http://contributor-covenant.org) code of conduct.

  1. Fork it ( https://github.com/addy3494/jc )
  1. Create your feature branch (`git checkout -b my-new-feature`)
  1. Commit your changes (`git commit -am 'Add some feature'`)
  1. Push to the branch (`git push origin my-new-feature`)
  1. Create a new Pull Request

***
## Author
* **gh0s1** - *Owner* - [addy3494]( https://github.com/addy3494 )
***
## Credits

  This project makes use
  * [pyfzf](https://github.com/nk412/pyfzf)
  * [fzf](https://github.com/junegunn/fzf)

***
The project is available as open source under the terms of the [MIT License](LICENSE)
