#! /usr/bin/env python

import argparse,logging,os,csv
from xsede_instprop import jetinstance
from xsede_volume import jetvolume
from xsede_action import jetaction
from os.path import expanduser
import getpass
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def jetstream_key_entry():
    jethome=expanduser("~/.config/jetstream/")
    if not os.path.exists(jethome):
        os.mkdir(jethome)
    print("Enter your JetStream Password")
    password=getpass.getpass()
    os.chdir(jethome)
    with open("jkey.csv",'w') as completed:
        writer=csv.writer(completed,delimiter=',',lineterminator='\n')
        writer.writerow([password])
def jetstream_key_from_parser(args):
    jetstream_key_entry()
def jetinstance_from_parser(args):
    jkey=expanduser("~/.config/jetstream/jkey.csv")
    if os.path.isfile(jkey):
        f=open(jkey)
        for row in csv.reader(f):
            passwd=str(row).strip("[']")
            jetinstance(username=args.username,password=passwd)
    else:
        jetinstance(username=args.username,password=getpass.getpass())
def jetvolume_from_parser(args):
    jkey=expanduser("~/.config/jetstream/jkey.csv")
    f=open(jkey)
    if os.path.isfile(jkey):
        f=open(jkey)
        for row in csv.reader(f):
            passwd=str(row).strip("[']")
            jetvolume(username=args.username,password=passwd)
    else:
        jetvolume(username=args.username,password=getpass.getpass())
def jetaction_from_parser(args):
    jkey=expanduser("~/.config/jetstream/jkey.csv")
    f=open(jkey)
    if os.path.isfile(jkey):
        f=open(jkey)
        for row in csv.reader(f):
            passwd=str(row).strip("[']")
            jetaction(username=args.username,instid=args.id,act=args.action,password=passwd)
    else:
        jetaction(username=args.username,instid=args.id,act=args.action,password=getpass.getpass())

spacing="                               "
def main(args=None):
    parser = argparse.ArgumentParser(description='JetStream API Unofficial')

    subparsers = parser.add_subparsers()
    parser_pp1 = subparsers.add_parser(' ', help='-------------------------------------------')
    parser_P = subparsers.add_parser(' ', help='-----Choose from JetStream Tools Below-----')
    parser_pp2 = subparsers.add_parser(' ', help='-------------------------------------------')

    parser_jetstream_key = subparsers.add_parser('jskey', help='Allows you to save your JetStream API Password')
    parser_jetstream_key.set_defaults(func=jetstream_key_from_parser)
    
    parser_jetinstance = subparsers.add_parser('instance', help='Allows users to print out all instance information')
    parser_jetinstance.add_argument('--username', help='Jetstream API username',default=None)
    parser_jetinstance.add_argument('--password', help='Jetstream API password: "Optional if you already saved jetstream key"',default=None)
    parser_jetinstance.set_defaults(func=jetinstance_from_parser)

    parser_jetvolume = subparsers.add_parser('volume', help='Allows users to print out all volume information')
    parser_jetvolume.add_argument('--username', help='Jetstream API username',default=None)
    parser_jetvolume.add_argument('--password', help='Jetstream API password: "Optional if you already saved jetstream key"',default=None)
    parser_jetvolume.set_defaults(func=jetvolume_from_parser)

    parser_jetaction = subparsers.add_parser('action', help='Allows user to start, suspend,resume,reboot instance')
    parser_jetaction.add_argument('--username', help='Jetstream API username',default=None)
    parser_jetaction.add_argument('--password', help='Jetstream API password: "Optional if you already saved jetstream key"',default=None)
    parser_jetaction.add_argument('--id', help='Jetstream Instance ID on your Instance Detail Page',default=None)
    parser_jetaction.add_argument('--action', help='Jetstream Instance Action, "start|stop|suspend|resume|reboot"',default=None)
    parser_jetaction.set_defaults(func=jetaction_from_parser)

    args = parser.parse_args()

    args.func(args)

if __name__ == '__main__':
    main()
