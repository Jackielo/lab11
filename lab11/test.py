import urllib2
import boto

req = urllib2.Request('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
f = urllib2.urlopen(req)
code = f.read()
access, key = code.split(":")
print(access + "\n" + key + "\n" + boto.Version)
