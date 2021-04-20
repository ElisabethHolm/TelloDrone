from tello import Tello
import sys
from datetime import datetime
import time
import argparse

#cd Downloads/Coding/TelloDrone/auto_flight
#python app.py

'''
def parse_args(args):
    """
    Parses arguments.
    :param args: Arguments.
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser('Tello Flight Commander', 
        epilog='One-Off Coder https://www.oneoffcoder.com')

    parser.add_argument('-f', '--file', help='command file', required=True)
    return parser.parse_args(args)
'''

#def start(file_name):
def start():
    print('started')
    """
    Starts sending commands to Tello.
    :param file_name: File name where commands are located.
    :return: None.
    """
    start_time = str(datetime.now())

    #with open(file_name, 'r') as f:
        #commands = f.readlines()

    commands = [
        "command",
        "battery?",
        "takeoff",
        "delay 2",
        "left 25",
        "right 25",
        "down 50",
        "delay 2",
        "land",
        "battery?"
    ]

    tello = Tello()
    for command in commands:
        print("running thru commands")
        #if command != '' and command != '\n':
            #command = command.rstrip()

        #if there is a delay command
        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print(f'delay {sec}')
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)
            #print("asking for response")
            #response = tello.get_response()
            #print("Here is the drone response")
            #print(response)
                

    with open(f'log.{start_time}.txt', 'w') as out:
        log = tello.get_log()

        for stat in log:
            stat.print_stats()
            s = stat.return_stats()
            out.write(s)


if __name__ == '__main__':
    #args = parse_args(sys.argv[1:])
    #file_name = args.file
    #start(file_name)
    start()
