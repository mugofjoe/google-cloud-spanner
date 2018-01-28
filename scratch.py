#!/usr/bin/env python

MY_TEXT = "Hello"

def test():
    MY_TEXT = "Changed"
    print "Inside test" + " " + MY_TEXT
    return MY_TEXT



if __name__ == '__main__':
    print MY_TEXT
    new_text = test()
    print "MY_TEXT is " + " " + MY_TEXT
    print "new_text is " + " " + new_text