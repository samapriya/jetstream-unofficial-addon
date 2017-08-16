# Jetstream Unofficial Addon for Atmosphere VM(s)
[![Jetstream](https://img.shields.io/badge/SupportedBy%3A-JetStream-brightgreen.svg)](https://jetstream-cloud.org/)

Jetstream provides researchers and students with a unique approach to cloud computing and data analysis on demand. Moving away from a job submission model which is more pervasice on High Performance Cluster computing this allows users to create user-friendly installs of “virtual machines” which can then be custom installed with softwares and packages and even imaged further to make science replicable. The system in theory also allows a BYoOS (Bring your own Operating System) designed to further allow more flexibility while sharing the backbone of high performance compute and cloud storage infrastructure. The idea of imaging a system allows the user to not only share their data or analysis but their entire setup that allows them to run the analysis making it a plug and play model in terms of research replication and transference. As the NSF project proceeds further it allows users to apply for grants or allocation time on the machines and indeed renew these free of cost for researchers and students. 

For my work looking at developing a Satellite Imagery Input Output (IO) pipeline I was allocated a Jetstream grant and while using a couple of these systems I always thought it would be easier to query number of instances and volumes running on my account, my burn rate and left over allocation over sometime. And something useful was the possibility to perform system actions such as shutdown(stop), restart, start, reboot among others programatically. It is with this idea that I approach the API backend at JetStream and built just a few tools to allows users to perform these actions without the need to log into their web browsers and allows user to call upon instance actions through a rough command line interface (CLI).

I would love to thank Steve Gregory who is getting the Official API ready for release and Jeremy Fischer who have helped me in more ways and allowed me to keep asking questions and learn from them to build the unofficial api for Jetstream.

The Jetstream's mission and funding is supported by NSF and any and all citations are useful so please make sure to cite and citation information can be found at the end of this readme or use the [link](https://jetstream-cloud.org/research/citing-jetstream.php)

*Note: I have used this on the Jetstream-IU system but it should work on the TACC end as well and the information I decided to show per instance is based on what I used, there are much more information generated but the tool prints a subset*

![CLI](http://i.imgur.com/52eJzp6.gif)

## Table of contents
* [Getting started](#getting-started)
    * [Save API Password as Credential](#save-api-password-as-credential)
    * [Query Current Instances](#query-current-instances)
    * [Query Current Volumes](#query-current-volumes)
    * [Perform Instance Actions](#perform-instance-actions)

## Getting started
To get started you need an XSEDE account of a Jetstream Rapid Access Account and you can create one using instructions [here](https://iujetstream.atlassian.net/wiki/display/JWT/Get+a+Jetstream+Rapid+Access+account). Once into the system you will still need an allocation and the wiki page setup by the project explains these along with everything you can do step by step [here](https://iujetstream.atlassian.net/wiki/spaces/JWT/overview). Once you have a project allocation and create some instances and volumes you can query and perform instance actions.

Just browse to the folder and perform a `python jetstream.py -h`:
```
usage: jetstream.py [-h] { ,jskey,instance,volume,action} ...

JetStream API Unofficial

positional arguments:
  { ,jskey,instance,volume,action}
                        -------------------------------------------
                        -----Choose from JetStream Tools Below-----
                        -------------------------------------------
    jskey               Allows you to save your JetStream API Password
    instance            Allows users to print out all instance information
    volume              Allows users to print out all volume information
    action              Allows user to start, suspend,resume,reboot instance

optional arguments:
  -h, --help            show this help message and exit

```

## Save API Password as Credential
This tool allows the user to save the credential or password file into ```users/.config/jetstream``` making sure that they are user specific and are not shared on a system resource or location. This password is not your XSEDE or Jetstream Rapid Access account password but a API password which has to be requested atleast for now. It uses a getpass implementation and write the password as a csv and the other tools first tries to read this and if not present asks for your password.

```
usage: jetstream.py jskey [-h]

optional arguments:
  -h, --help  show this help message and exit

```



### Query Current Instances
As the name stated this allows the user to query 

```

```
An example setup would be
```

```



## Download DEM


```

```
An example setup would be
```
arcticdem demdownload --subset "C:\users\master_aoi.shp" --destination "C:\users\ArcticDEM"
```
 
## Extract DEM


```

```
An example setup would be
```
arcticdem demdextract --folder "C:\users\ArcticDEM" --destination "C:\users\ArcticDEM\Extract" --action "yes"
```
