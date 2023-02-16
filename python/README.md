## Script Usage
- Note that all the scripts are intended for Linux system environment. Also confirm if the task require using of library or pure python before proceeding. Before using any script at all, always consider the following points;
- Understand the task to achieve
- Flesh out the task in details
- Gather and understand all the commands, concepts, logics, statements, function, modules needed to achieve the task
- Sequentially write the instructions, saved in a file, module or package it
- Make the file, package executable for users
- Adjust the file, package path

Peace!

## Documentations
https://pypi.org/project/boto3/
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
https://docs.python.org/3/library/smtplib.html
https://docs.python.org/3/library/time.html

## Connect to Boto3
- Before using Boto3, we need to set up authentication credentials for my AWS account.
- The library provides an object-oriented API as well as low-level access to AWS services

## Terraform vs Python
- When to use python;
Python can also be used for infrastructure provisioning, but Terraform is much better for this use case.

|  Terraform | Python |
| --- | --- |
| TF manages state of the infrastructure, so TF knows the current state | Python doesn't have a state and is not idempotent |
| TF knows the difference of current and your configured/desired state | In TF you declare the end result, while in Python you need to explicitly write what you want to do (imperative) |
| TF is idempotent (multiple execution of same config file, will aways result in same end result) | Python is more low level, so it's more flexible and you can write very complex logic: Monitoring, BackUps, Scheduled Task |


## Some Basic Modules
Battery included - Module for almost everything
The following are installed by default(for details, check https://doc.python.org/3/library);
os - interact with operating system
sys - functions and variable, create directories in pipeline
re - regular expression matching, patterns and strings, shorten and speed-up code
subprocess - spawn new process
Platform - Device, OS, Version, Python
smptplib - send emails with SMTP
The following need to be installed;
Requests - http request (learn more at https://pypi.org/project/requests)
Beautiful Soup - Scrape info from web pages (learn more at https://pypi.org/project/beautifulsoup4)
Fabric - (learn more at fabfile.org)
