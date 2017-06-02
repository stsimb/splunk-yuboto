## Splunk Yuboto Modular Alert v1.0

## Overview

This is a Splunk Modular Alert for sending SMS messages using Yuboto.

## Dependencies

* Splunk 6.3+
* Supported on Windows, Linux, MacOS, Solaris, FreeBSD, HP-UX, AIX.

## Setup

* Untar the release to your $SPLUNK_HOME/etc/apps directory.
* Restart Splunk.

## Configuration

You will need a Yuboto account to use this Modular Alert.

You can sign up at yuboto.com.

Once your Yuboto account is setup you will then be able to obtain your API key from your profile.

To enter these values in Splunk, just browse to Settings -> Alert Actions -> Yuboto SMS Alerts -> Setup Yuboto SMS Alerting.

## Using

Perform a search in Splunk and then navigate to : Save As -> Alert -> Trigger Actions -> Add Actions -> Yuboto SMS Alerts.

On this dialogue you can enter your "to number" and "SMS message".

"to number" can also be a comma delimited list of numbers.

For the SMS message field, token substitution can be used just the same as for email alerts.

http://docs.splunk.com/Documentation/Splunk/latest/Alert/EmailNotificationTokens

## Logging

Browse to : Settings -> Alert Actions -> Yuboto SMS Alerts -> View Log Events

Or you can search directly in Splunk: index=_internal sourcetype=splunkd component=sendmodalert action="yuboto"


## Troubleshooting

1. Is your "from number" correct and valid for sending SMS messages via Yuboto ?
   Length of sender must be 16 digits numeric or 11 digits alphanumeric.
2. Id your API key correct ?
3. Are your alerts actually firing ?

