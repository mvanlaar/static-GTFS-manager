import json
import os,platform,requests

from settings import appconfig
requests.packages.urllib3.disable_warnings() # suppress warning messages like "InsecureRequestWarning: Unverified HTTPS request is being made." from https://stackoverflow.com/a/44850849/4355695

def logUse(action='launch'):
	if 'APP' in appconfig:
		if 'Tracking' in appconfig['APP']:
			if appconfig['APP']['Tracking'] == 'true':
				payload = {'idsite': 3,  'rec': 1, 'send_image':0}
				payload['action_name'] = action
				cvar = {}
				cvar['1'] = ['OS', platform.system()]
				cvar['2'] = ['processor',platform.processor()]
				#TODO: For Python 3.7 compat remove the use of .linuxdistribution.
				if cvar['1'][1] == 'Linux':
					cvar['1'][1] = platform.linux_distribution()[0]
					cvar['3'] = ['version', platform.linux_distribution()[1] ]
				else:
					cvar['3'] = ['version', platform.release() ]
				payload['_cvar'] = json.dumps(cvar)
				try:
					r = requests.get('https://nikhilvj.co.in/tracking/piwik.php', params=payload, verify=False, timeout=1)
				except requests.exceptions.RequestException as e:
					# print('exception',e)
					pass