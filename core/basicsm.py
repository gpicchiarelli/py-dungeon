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

from state_machine import *


@acts_as_state_machine
class BasicSM():
    name = 'default'
    initialize = State(initial=True)
    setup = State()
    running = State()
    gone = State()

    init = Event(from_states=(initialize), to_state=setup)
    run = Event(from_states=(setup), to_state=running)
    close = Event(from_states=(running), to_state=gone)

    def __init__(self, description):
        if type(self) is BasicSM:
            raise NotImplementedError("BasicSM can't be instantiated")
        self.name = name = description
        self.init()

    @before('init')
    def beforeInit(self):
        print(self.name + ' -- beforeInit')

    @before('run')
    def beforeRun(self):
        print('beforeRun')

    @before('close')
    def beforeClose(self):
        print('beforeClose')


""" Usage Example
bm = BasicSM('try')
bm.run()
bm.close()
"""
