#!/usr/bin/env python3                                                
"""
   BSD 3-Clause License
   
   Copyright (c) 2019, Giacomo Picchiarelli
   All rights reserved.
   
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
  
  1. Redistributions of source code must retain the above copyright notice, this
     list of conditions and the following disclaimer.
  
  2. Redistributions in binary form must reproduce the above copyright notice,
     this list of conditions and the following disclaimer in the documentation
     and/or other materials provided with the distribution.
  
   3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
import os
import io
import signal

class Daemon:
	def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
		if type(self) is BasicSM: 
			raise NotImplementedError("Daemon can't be instantiated")
		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr
		self.pidfile = pidfile
		
	def daemonize(self,stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
		try: 
			pid = os.fork() 
			if pid > 0:
				sys.exit(0)
			fd = open(self.pidfile,'w')
			fd.write(str(pid))
		except OSError as e: 
			sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )
			sys.exit(1)
		os.chdir("/") 
		os.umask(0) 
		os.setsid() 

		try: 
			pid = os.fork() 
			if pid > 0:
				sys.exit(0)
			fd = open(self.pidfile,'w')
			fd.write(str(pid))
		except OSError as e: 
			sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )
			sys.exit(1)

		stdin_par = os.path.dirname(stdin)
		stdout_par = os.path.dirname(stdout)
		stderr_par = os.path.dirname(stderr)
		if not stdin_par:
			os.path.makedirs(stdin_par)
		if not stdout_par:
			os.path.makedirs(stdout_par)
		if not stderr_par:
			os.path.makedirs(stderr_par)
			
		si = open(stdin, 'r')
		so = open(stdout, 'a+')
		se = open(stderr, 'a+')
		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())

	def set_procname(self,name):
		import ctypes
		lc = ctypes.cdll.LoadLibrary("libc.so.95.0")
		lc.prctl(15, name[:15])

	def delpid(self):
		os.remove(self.pidfile)

	def start(self):
		"""
		Start the daemon
		"""
		# Check for a pidfile to see if the daemon already runs
		try:
			pf = open(self.pidfile,'r')
			pid = pf.read()
			pf.close()
		except IOError as e:
			pid = None

		if pid:
			message = "pidfile %s already exist. Daemon already running?\n"
			sys.stderr.write(message % self.pidfile)
			sys.exit(1)

		# Start the daemon
		self.daemonize()
		self.run()

	def stop(self):
		"""
		Stop the daemon
		"""
		# Get the pid from the pidfile
		try:			
			pf = open(self.pidfile,'r')
			pid = int(pf.read().strip())
			pf.close()
			pid = True
		except IOError as e:
			pid = False
			print(e)

		if not pid:
			message = "pidfile %s does not exist. Daemon not running?\n"
			sys.stderr.write(message % self.pidfile)
			return # not an error in a restart

		# Try killing the daemon process       
		try:
			os.kill(pid, signal.SIGTERM)
		except OSError as err:
				err = str(err)
				if err.find("No such process") > 0:
					if os.path.exists(self.pidfile):
							os.remove(self.pidfile)
				else:
					print(err)
					sys.exit(1)

	def restart(self):
		"""
		Restart the daemon
		"""
		self.stop()
		self.start()

	def run(self):
		"""
		To override with a subclass
		"""
