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
   ad/or other materials provided with the distribution.
   
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

import cmd,socket,re,sys

class CoreCLI(cmd.Cmd):
	""" py-dungeond daemon console """

	def __init__(self):
		self.prompt = 'dungeond$ '
		self.intro = 'Welcome to the dungeond shell. Waiting for orders.'
		self.use_raw_input = True
		self.completekey = 'tab'
		self.stdout = sys.stdout
		self.stdin = sys.stdin
		self.cmdqueue = ['']
		
	def do_quit(self, args):
		"""Quits the shell."""
		print("Quitting.")
		return True
	
	def do_module(self, args):
		"""module control. Example module <name> check|start|stop"""
		tm = re.sub('\s+', ' ', args).strip()
		arg = tm.split(' ')
		if(len(arg) == 2):
			module_name = arg[0]
			if(arg[1] == 'check'):
				print(arg[0])
				print(arg[1])
			elif(arg[1] == 'start'):
				print(arg[0])
				print(arg[1])
			elif(arg[1] == 'stop'):
				print(arg[0])
				print(arg[1])
			else:
				print("Syntax error: module control.")
				print("Example: module <name> check|start|stop")
		else:
			print("Syntax error: module control.")
			print("Example: module <name> check|start|stop")

if __name__ == "__main__" :
	cli = CoreCLI()
	cli.cmdloop()
