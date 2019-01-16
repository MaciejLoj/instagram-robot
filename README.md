# Basic Instagram bot created using Python and Selenium WebDriver
> It's a project entirely developed by myself. It presents a simple Instagram bot that can either
like, comment on photos or even follow by given hashtag. What is more it can unfollow accounts
that do not follow you.


## General info
The main purpose of the project is to help my friend to boost popularity of her Instagram account


## Technologies I used
* OS: macOS
* Python Version: 3.6
* Selenium Version: 3.14.0
* Web browser: Mozilla Firefox Quantum 63.0.3 (64-bit)
* GeckoDriver

Bot should also work on other versions so just download mentioned programs and run the
code in your IDE
## Setup

 All you need to do is to have Python, Selenium and GeckoDriver installed.

 If you do not have Selenium, Python 3.6 has pip available in the standard library
 so you can install it easily:

`pip install selenium`


To download GeckoDriver:

I. Go to [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
and download file for your system.

II. Unzip it

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver,
which needs to be installed before the below examples can be run.
Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.


III. Open Terminal and go to the directory where you unzipped geckodriver file:
For example:

`cd Desktop`

IV. move your file to above-mentioned PATH

`mv nameofthefile /usr/bin`

or if it doesn't work

`mv nameofthefile /usr/local/bin`



V. If something went wrong just go to below page and read everything carefully

[https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)


That's it!

## Code Examples
Example of usage:

I. Creates an account with given login and password

`user1 = InstaRobot("login","password")`

II. Logs in to your account

`user1.login()`

III. Finds photos by given hashtag, likes and comments on photos by given hashtag, and finally follows accounts
by given hashtag.
All you need to do is to set amount of photos to follow and add type of comments you want the bot to type in.
Those features will be added in the Python file, so you can adjust them however you want!

`user1.find_photos("hashtag")`

IV. Creates a list of your followers

`user1.my_followers()`

V. Creates a list of accounts you follow

`user1.am_following()`

VI. Compares lists and unfollows accounts that do not follow you. (IV and V are needed)

`user1.accounts_to_unfollow()`

## Features
List of features ready:
* Likes photos by given hashtag
* Comments on photos by given hashtag
* Follows accounts by given hashtag
* Unfollow accounts that do not follow you

TODOs for future development:
* Need to improve code with regard to unfollowing speed. It works fine but is time-consuming.


## Status
Project is: _almost finished_


## Contact
Created by Loju - feel free to contact me!
[email](mailto:maciej.loj@gmail.com)
