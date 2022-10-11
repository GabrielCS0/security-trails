# About

This is a tool to automate the search for subdomains on the website [securitytrails.com](https://securitytrails.com/).

See it in action:

```
$ python3 st.py -d hackerone.com -k aR1v4erPY3fdcpCi9ngk0WSzr7r9YJz0  

[*] Searching securitytrails.com for subdomains of hackerone.com
[*] Found 20 subdomains of hackerone.com

api.hackerone.com
docs.hackerone.com
support.hackerone.com
defcon.hackerone.com
mta-sts.managed.hackerone.com
web-seo-content-for-business.theflyingkick.websitedesignresource.api.hackerone.com
zendesk1.hackerone.com
zendesk2.hackerone.com
a.ns.hackerone.com
resources.hackerone.com
email.gh-mail.hackerone.com
mta-sts.forwarding.hackerone.com
design.hackerone.com
events.hackerone.com
zendesk4.hackerone.com
zendesk3.hackerone.com
gslink.hackerone.com
b.ns.hackerone.com
www.hackerone.com
mta-sts.hackerone.com
```

*Use your own API KEY, this one will not work.

## Setup

1) Clone the repository

```
git clone https://github.com/GabrielCS0/security-trails.git
```

2) Install the dependencies in a virtualenv

```
cd security-trails
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-h            | --help        | Show a help message.
-d            | --domain      | The domain to be searched.
-k            | --api-key     | Your Securitytrails API Key.
-o            | --output      | The text file to save the results.
