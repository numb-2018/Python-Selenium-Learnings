#!C:\Users\asingh\PycharmProjects\SeleniumBDD\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyTextUtil==0.0.6','console_scripts','pyTextUtil'
__requires__ = 'pyTextUtil==0.0.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyTextUtil==0.0.6', 'console_scripts', 'pyTextUtil')()
    )
