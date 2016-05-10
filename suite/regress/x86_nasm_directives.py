#!/usr/bin/python
# Nguyen Anh Quynh, 2016

# This is to test NASM directives

# Fill in the information in the form below when you create a new regression

# Github issue: #xxx
# Author: Nguyen Anh Quynh

from keystone import *

import regress

class TestX86(regress.RegressTest):
    def runTest(self):
        # Initialize Keystone engine
        ks = Ks(KS_ARCH_X86, KS_MODE_32)
        # change the syntax to NASM
        ks.syntax = KS_OPT_SYNTAX_NASM

        # compile an instruction in NASM syntax
        #encoding, count = ks.asm(b"bits 32\n add eax, ebx\nbits 16\nadd eax, ebx")
        encoding, count = ks.asm(b"bits 32\n add eax, ebx\nbits 16\nadd eax, ebx")
        # Assert the result
        self.assertEqual(encoding, [ 0x01, 0xd8, 0x66, 0x01, 0xd8 ])

if __name__ == '__main__':
    regress.main()