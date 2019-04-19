import json
import sys
from getpass import getuser
from urllib.parse import quote_plus
from webbrowser import open_new_tab

import boto3
import requests


def go(profile_name, duration):
    session = boto3.session.Session(profile_name=profile_name)
    sts = session.client('sts')
    issuer = f'{profile_name}-easy-aws-login'
    try:
        name = f'{getuser()}-{issuer}'
        if len(name) > 32:
            name = name[:32]
        response = sts.get_federation_token(Name=name, DurationSeconds=duration, Policy=json.dumps({
            'Version': '2012-10-17',
            'Statement': [{
                'Action': '*',
                'Effect': 'Allow',
                'Resource': '*'
            }]
        }))
    except:
        role_arn = session._session._profile_map[profile_name]['role_arn']
        response = sts.assume_role(RoleSessionName=issuer, DurationSeconds=duration, RoleArn=role_arn)
    json_temp_credentials = json.dumps({'sessionId': response['Credentials']['AccessKeyId'],
                                        'sessionKey': response['Credentials']['SecretAccessKey'],
                                        'sessionToken': response['Credentials']['SessionToken']})

    quote_session = quote_plus(json_temp_credentials)
    get_token_url = f"https://signin.aws.amazon.com/federation?Action=getSigninToken&Session={quote_session}"
    sign_in_token = requests.get(get_token_url).json()['SigninToken']

    destination = quote_plus('https://console.aws.amazon.com/')
    sign_in_url = f"https://signin.aws.amazon.com/federation?Action=login&Issuer={issuer}&Destination={destination}&SigninToken={sign_in_token}"
    try:
        open_new_tab(sign_in_url)
    except:
        print('Could not automatically open browser. Click the following link to sign in:')
        print(sign_in_url)


def main():
    profile_name = 'default' if len(sys.argv) < 2 else sys.argv[1]
    duration = 3600 if len(sys.argv) < 3 else int(sys.argv[2])
    if duration < 900:
        raise Exception('Duration must be at least 900 seconds')
    go(profile_name, duration)


if __name__ == '__main__':
    main()
