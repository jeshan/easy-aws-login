# easy-aws-login
[![PyPI version](https://badge.fury.io/py/easy-aws-login.svg)](https://badge.fury.io/py/easy-aws-login)
![Build badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoia2s2SzRNemtBQ2pIOWVVN2x6S3NnQWwrdGR1V001R1hhRmtESmdNZVVEaVhyMUV3WnNrWDhtVHFJcFdYeHdZbnhQQklXcyttei9BeVJCZnB3NU5iM0N3PSIsIml2UGFyYW1ldGVyU3BlYyI6IjRoUEN1dVZmTlVuekNWL0MiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

The easiest way to log in to your AWS console. Get started by running `pip install easy-aws-login`

Leverages the existing `aws-cli` profiles that you've already set up.

Also clearly shows which profile (hence account) the user is in.

![example](screenshot1.png)


to login with your default credentials, type:
`easy-aws-login`


to login with a profile, type:
`easy-aws-login my-profile`


to login with a profile and change the default session duration of 12 hours (43200 seconds), type:
`easy-aws-login my-profile 7200`


## Deployment
This project is managed by AWS CodeBuild and the cloudformation template that drives it is found under [templates/deployment-pipeline.yaml](templates/deployment-pipeline.yaml). This is what a visualisation of it looks like:

![](/diagram.png)
