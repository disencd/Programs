#!/usr/local/bin/python2.7

import dpkt
import sys,getopt

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

#filename='sip_volte'

def parse_pcap_file(filename):
    global counter, ipcounter, tcpcounter, udpcounter

    for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):

        counter+=1
        eth=dpkt.ethernet.Ethernet(pkt)
        if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
            continue

        ip=eth.data
        ipcounter+=1

        if ip.p==dpkt.ip.IP_PROTO_TCP:
            tcpcounter+=1

        if ip.p==dpkt.ip.IP_PROTO_UDP:
            udpcounter+=1

        transport = ip.data

        if transport.sport == 5060 or transport.sport == 5061:
            print("Sip Message ", transport.data)


    print "Total number of packets in the pcap file: ", counter
    print "Total number of ip packets: ", ipcounter
    print "Total number of tcp packets: ", tcpcounter
    print "Total number of udp packets: ", udpcounter


if __name__ == "__main__":
    ifile = ''
    ofile = ''

    ###############################
    # o == option
    # a == argument passed to the o
    ###############################
    # Cache an error with try..except
    # Note: options is the string of option letters that the script wants to recognize, with
    # options that require an argument followed by a colon (':') i.e. -i fileName
    #
    try:
        myopts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -i input -o output" % sys.argv[0])
        sys.exit(2)

    for o, a in myopts:
        if o == '-i':
            parse_pcap_file(a)

        else:
            print("Usage: %s -i input -o output" % sys.argv[0])
            sys.exit(2)


