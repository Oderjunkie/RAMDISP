#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def execcode(source):
    scopes = [[]]

    for char in source:
        if char=='[':
            scopes.append([])
        elif char==']':
            scopes[-2].append(scopes.pop())
        else:
            scopes[-1].append(char)

    output = scopes[0][0]

    def find_val(origarr):
        arr = origarr
        depth = 0
        while len(arr)==1:
            arr = arr[0]
            depth += 1
        #print(arr)
        if len(arr)==0:
            return depth
        else:
            return origarr

    def parseval(part):
        #print(part)
        if part==':':
            return int(input('Input an integer: '))
        if type(part)==list:
            return find_val(part)
        return int(part)

    class Range:
        def __init__(self, val):
            self.current = 0
            self.val = val
        def __iter__(self):
            return self
        def __next__(self):
            self.current += 1
            if self.current==self.val+1: #INTENTIONAL, so Range(-x) makes an infinite loop.
                raise StopIteration
            return self.current

    class AntiRange:
        def __init__(self, val):
            self.current = val+1
            self.val = val
        def __iter__(self):
            return self
        def __next__(self):
            self.current -= 1
            if self.current==0:
                raise StopIteration
            return self.current

    def anti(tree):
        if type(tree)==Range:
            return AntiRange(tree.val)
        if type(tree)==list:
            return [anti(branch) for branch in tree[::-1]]
        else:
            return tree

    def parsefunccall(func, args):
        #print('CALLING {} WITH {}'.format(func, args))
        if func=='P':
            rolling = parseval(args[0])
            for part in args[1:]:
                #print(part[1:], rolling)
                rolling = parsefunccall(part[0], [*part[1:], rolling])
            return rolling
        if func=='D':
            arr = []
            for part in args[0]:
                #print(part)
                arr.append(parsefunccall(part[0], [*part[1:], *args[1:]]))
            return arr
        if func==';':
            return print(end=''.join(map(str, args)))
        if func=='I':
            return parsefunccall(args[0][0], args[0][1:])
        if func=='S':
            lastarg = args[1]
            func, *args = args[0]
            return parsefunccall(func, [lastarg, *args])
        if func=='R':
            return Range(args[0])
        if func=='A':
            return anti(args[0])
        if func=='M':
            return [parsefunccall(args[0][0], [*args[0][1:], val]) for val in args[1]]
        if func=='~':
            return -parseval(args[0])
        if func=='-':
            return parseval(args[0]) - parseval(args[1])
        if func=='+':
            return parseval(args[0]) + parseval(args[1])
        if func=='*':
            return parseval(args[0]) * parseval(args[1])
        if func=='/':
            return parseval(args[0]) // parseval(args[1])
        if func=='%':
            return parseval(args[0]) % parseval(args[1])

    parsefunccall(*output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', metavar='in_file', type=str,
                        help='The input RAMDISP file')
    args = parser.parse_args()
    with open(args.input, 'r') as f:
        execcode(f.read())
