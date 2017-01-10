### README for nagios-plugins-apache-threads

You can use this check by configuring in nconf/nagios a checkcommand with a check command line of:
$USER1$/check_by_ssh -H $HOSTADDRESS$ -C "$USER1$/check_apache_threads -w $ARG1$ -c $ARG2$"

Some sample default values for -w and -c are 50 and 150, respectively.

### LICENSE
CC-BY-SA 4.0

### INSTALL
Nothing special.
