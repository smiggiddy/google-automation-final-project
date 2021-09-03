#!/usr/bin/env python3

"""
Script will do the requested pc checks
"""
import shutil
import psutil
import sys
import socket
import emails

def check_cpu_usage():
    #Checks CPU percentage and returns error if over 80%
    cpu_load = psutil.cpu_percent(interval=1)
    return cpu_load < 80


def check_mem_usage():
    #checks if only 500MB ram left
    mem = psutil.virtual_memory()
    return (mem.available / 1024 ** 2) > 500

def check_root_full():
    """ Function checks if disk usage is
    over 80% used
    """
    disk_usage = shutil.disk_usage("/")
    free = disk_usage.free / disk_usage.total * 100
    return free > 20


def check_no_network():
    #Checks if localhost resolves to loopback
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"



def main():

    checks = [
    (check_cpu_usage, "Error - CPU usage is over 80%"),
    (check_root_full, "Error - Available disk space is less than 20%"),
    (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1"),
    (check_mem_usage, "Error - Available memory is less than 500MB")
    ]
    # print(check_cpu_usage())
    for check, msg in checks:
        if not check():
            print(msg)
            e_msg_email = emails.generate_error("automation@example.com","student-03-d4e234470c42@example.com",
            msg,
            "Please check your system and resolve the issue as soon as possible."
            )
            emails.send(e_msg_email)
        else:
            return True


if __name__ == '__main__':
    main()
