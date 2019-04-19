# easy-aws-login
The easiest way to log in to your AWS console. Get started by running `pip install easy-aws-login`

Leverages the existing `aws-cli` profiles that you've already set up.

Also clearly shows which profile (hence account) the user is in.

![See demo gif on github](https://raw.githubusercontent.com/jeshan/botostubs/master/screenshot1.png)


to login with your default credentials, type:
`easy-aws-login`


to login with a profile, type:
`easy-aws-login my-profile`


to login with a profile and change the default session duration of 3600 seconds, type:
`easy-aws-login my-profile 7200`
