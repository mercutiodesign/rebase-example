#!/usr/bin/env python3

def greeting():
    print('hello world')

def ask_for_name():
    name = input('please enter your name: ')
    print('hi', name)
    print('have a nice day!')

if __name__ == '__main__':
    greeting()
    ask_for_name()
