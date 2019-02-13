from __future__ import print_function

import subprocess
import sys


try:

	ssh = subprocess.Popen(["plink.exe", "-ssh", 
				"usename@servername.com",
				"-pw", "sshpassword",
				"-D", "1080"
				"-N"],
					shell=False,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
	p=subprocess.Popen(['Proxifier.exe'])

	result = ssh.stdout.readlines()

	error = ssh.stderr.readlines()					

except KeyboardInterrupt:
	p.kill()
	sys.exit()
	
