#!/usr/bin/env python
import os
print(f'{{"tag_name": "v{os.environ["CODE_VERSION"]}", "name": "{os.environ["CODE_VERSION"]}", "body": "Release number {os.environ["CODE_VERSION"]}"}}')

