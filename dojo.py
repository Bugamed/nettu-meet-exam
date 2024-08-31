import requests
import sys

file_name = sys.argv[1]
scan_type = ''

if file_name == 'trivy.json':
    scan_type = 'trivy Scan'
elif file_name == 'zap.json':
    scan_type = 'zap Scan'
elif file_name == 'semgrep.json':
    scan_type = 'Semgrep Scan'


headers = {
    'Authorization': 'Token c5b50032ffd2e0aa02e2ff56ac23f0e350af75b4'
}

url = 'https://s410-exam.cyber-ed.space:8083/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 19
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')
