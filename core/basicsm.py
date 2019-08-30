#!/usr/bin/env python3

"""
    4 BSD 3-Clause License
    5 Copyright (c) 2019, Giacomo Picchiarelli
    6 All rights reserved.
    7 Redistribution and use in source and binary forms, with or without
    8 modification, are permitted provided that the following conditions are met:
    9 1. Redistributions of source code must retain the above copyright notice, this
   10    list of conditions and the following disclaimer.
   11 2. Redistributions in binary form must reproduce the above copyright notice,
   12    this list of conditions and the following disclaimer in the documentation
   13    and/or other materials provided with the distribution.
   14 3. Neither the name of the copyright holder nor the names of its
   15    contributors may be used to endorse or promote products derived from
   16    this software without specific prior written permission.
   17 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   18 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   19 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
   20 DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
   21 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
   22 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
   23 SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
   24 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
   25 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
   26 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
   27 """
from state_machine import *

@acts_as_state_machine
class BasicSM(object):
    
    def __init__(self,name = 'BasicSM'):
        self.name = name
        self.init = State('init', initial=True)
        self.running = State('running')
        self.cleaning = State('cleaning')
        self.exit = State('exit')

    @event(from_state=(self.init), to_state=self.running)
    def initialize(self):
        pass

    @event(from_state=(self.running),to_state=self.cleaning)
    def run(self):
        pass

    @event(from_state(self.cleaning), to_state=self.exit)
    def cleanup(self):
        pass
"""
     self.run = Event(from_states=init, to_state=running)
     self.cleanup = Event(from_states=running, to_state=cleaning)
     self.sleep = Event(from_states=(running, cleaning), to_state=sleeping)

    @event(from_states=(locked, unlocked), to_state=unlocked)
    def coin(self):
        assert random.random() > .5, 'failing for demonstration purposes, only ..'
        print('*blingbling* .. unlocked!')

    @event(from_states=(locked, unlocked), to_state=locked)
    def push(self):
        print('*push* .. locked!')

    @transition_failure_handler(calling_sequence=2)
    def turnstile_malfunction(self, method, from_state, to_state, error):
        print('state transition from {0.name} to {1.name} failed. Reason: {2}'.format(from_state, to_state, error))

    @transition_failure_handler(calling_sequence=1)
    def before_turnstile_malfunction(self, method, from_state, to_state, error):
        print('before state transition failure handler ..')


Code to review. Taken from example.
    @event(from_states=(locked, unlocked), to_state=unlocked)
    def coin(self):
        assert random.random() > .5, 'failing for demonstration purposes, only ..'
        print('*blingbling* .. unlocked!')

    @event(from_states=(locked, unlocked), to_state=locked)
    def push(self):
        print('*push* .. locked!')

    @transition_failure_handler(calling_sequence=2)
    def turnstile_malfunction(self, method, from_state, to_state, error):
        print('state transition from {0.name} to {1.name} failed. Reason: {2}'.format(from_state, to_state, error))

    @transition_failure_handler(calling_sequence=1)
    def before_turnstile_malfunction(self, method, from_state, to_state, error):
        print('before state transition failure handler ..')


    @before('sleep')
    def do_one_thing(self):
        print "{} is sleepy".format(self.name)

    @before('sleep')
    def do_another_thing(self):
        print "{} is REALLY sleepy".format(self.name)

    @after('sleep')
    def snore(self):
        print "Zzzzzzzzzzzz"

    @after('sleep')
    def big_snore(self):
        print "Zzzzzzzzzzzzzzzzzzzzzz"
"""
