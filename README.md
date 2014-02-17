anyone.py
=========

## Getting started

    git clone https://github.com/bitprinter/anyone.git anyone
    cd anyone
    ./load.py ; ./test.py # Make sure all tests pass!


## Interface

    usage: anyone.py [-h] [-a, --age AGE] [--min-age MIN_AGE] [--max-age MAX_AGE]
                     [-s, --state {AK..WY} | -z, --zip-code ZIP]
                     [-m, --male | -f, --female] [-c, --common {1..5}]

    Create a random identity.

    optional arguments:
      -h, --help            show this help message and exit
      -a, --age AGE         Specify an age, overrides --min-age and --max-age
      --min-age MIN_AGE     Specify a minimum age (default: 25)
      --max-age MAX_AGE     Specify a maximum age (default: 75)
      -s, --state {AK..WY}  Specify a state
      -z, --zip-code ZIP    Specify a zip-code
      -m, --male            Choose from masculine first names
      -f, --female          Choose from feminine first names
      -c, --common {1..5}   Likelihood of common values (default: 3)


## Target Feature-set (many incomplete)

* Last name, First name
* Address
* Phone Number
* Birthday
* Birthplace
* SSN

* Sex
* Height
* Weight
* Hair color
* Eye color
* Blood type

* Email Address
* Username
* Secure Password
* Insecure Password
* Passphrase

* Mother's maiden name
* Occupation
* Credit card Info (Issuer / Number / Exp. Date / CVC)
* Vehicle
