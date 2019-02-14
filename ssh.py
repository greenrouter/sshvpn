from __future__ import print_function

import subprocess
import sys
import time

yy="y"

try:

	ssh = subprocess.Popen(["plink.exe", "-ssh", 
				"username@servername.com",
				"-pw", "passwordssh",
				"-D", "1080"
				"-N"],
					shell=False,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
	

	print("Press y to accept the communication key...")
	keyval = raw_input()
	if keyval==yy:
		print("connected and openned socks5 in 127.0.0.1:1080")
		print("press ctrl+c to exit")

	else:
		sys.exit()
		
	
	p=subprocess.Popen(['Proxifier.exe'])
	result = ssh.stdout.readlines()
	error = ssh.stderr.readlines()	



except KeyboardInterrupt:
	p.kill()
	sys.exit()
	
