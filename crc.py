#!/usr/bin/env python
from pycrc.crclib import *

def main():
#-----------------------------------------------------------------------------
#Sender

    user_dataword = str(raw_input("Input dataword in binary format: "))
    divisor = str(raw_input("Input divisor in binary format: "))
   
    #user_dataword = '11010011101100'
    
    print "\nSender:"
    
    sender = Sender(user_dataword, divisor)
    sender.send()
    
    print "arg_dataword:", sender.arg_dataword2
    print "remainder:", sender.remainder2
    print "codeword:", sender.codeword2
 
#-----------------------------------------------------------------------------
#Channel

    print "\nChannel:"

    channel = Channel(sender.codeword, rate=0.2)
    #Error Rate 20%, By Default 30%
    print "Throgh to the channel get channel codeword:", channel.ch_codeword2
     
#-----------------------------------------------------------------------------
#Receiver

    print "\nReceiver:"

    receiver = Receiver(channel.ch_codeword, divisor)

    receiver.receive()

    print "syndrome:", receiver.syndrome2
    print "Discard or not?", receiver.discard
    print "rx_dataword:", receiver.rx_dataword2

if __name__ == '__main__':
    main()