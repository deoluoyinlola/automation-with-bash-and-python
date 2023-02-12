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