#!/usr/bin/env python3

import os
import sys
import sqlite3
import argparse
from pyfzf.pyfzf import FzfPrompt
from pathlib import Path

# globals
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
fzf = FzfPrompt()


def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser()
    p_group = parser.add_mutually_exclusive_group()
    p_group.add_argument('-a', '--add', help="Add new connection entry", action="store_true")
    p_group.add_argument('-c', '--connect', help="Initate a intertactive connection menu", action="store_true")
    p_group.add_argument('-d', '--delete', help="Delete new connection entry", action="store_true")
    p_group.add_argument('-l', '--list', help="List all available entries", action="store_true")
    return parser.parse_args()


def initialize_db():
    config_dir = str(os.path.join(str(Path.home()), ".config/jc"))
    os.system("mkdir -p " + config_dir)
    db_file = os.path.join(config_dir, 'jc.db')
    connect = sqlite3.connect(db_file)
    cursor = connect.cursor()
    init(cursor)
    return [connect, cursor]


def init(cursor):
    cursor.execute(
        """CREATE TABLE if not exists main(environment text,hostname text,ip_address real,username text,
        password text)""")


def column_header(cursor):
    return [description[0] for description in cursor.execute('select * from main').description]


def column_separator(header):
    return [('-' * len(h)) for h in header]


def pretty_print(data, header, separator):
    widths = [len(cell) for cell in header]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = ' '.join('{:%d}' % width for width in widths)
    print('\t' + formatted_row.format(*header))
    print('\t' + formatted_row.format(*separator))
    for row in data:
        print('\t' + formatted_row.format(*row))


def insert_func(cursor, data):
    cursor.executemany("INSERT INTO main VALUES (?,?,?,?,?)", data)
    print("{} *> '{}' insert(s) {}successful{}".format(BOLD, len(data), OKGREEN, ENDC))


def add(cursor):
    header = column_header(cursor)
    separator = column_separator(header)
    print('{} *>  Do you have a file to load ?{}'.format(BOLD, ENDC))
    dec = input('{} *> [Y/N] :{} '.format(BOLD, ENDC))
    if dec.upper() == 'N':
        print(" *>  Enter the details in '{}{}{}' format".format(BOLD, header, ENDC))
        a_inpt = [input('  *> INPUT: ').split(',')]
    else:
        print('{} *> /path/to/file ?{}'.format(BOLD, ENDC))
        try:
            with open(input(), 'r') as file:
                a_inpt = [line.strip('\n').split(',') for line in file if not line.startswith('#') or line.startswith('\n')]
        except:
            print('{} *> {}file not found{}'.format(BOLD,FAIL,ENDC))
            exit(1)
    data = [tuple(d) for d in a_inpt]
    print('{} *> The below info will be added, proceed ?{}\n'.format(BOLD, ENDC))
    pretty_print(data, header, separator)
    dec = input('{}\n *> [Y/N] :{} '.format(BOLD, ENDC))
    if dec.upper() == 'Y':
        insert_func(cursor, data)


def connect(cursor):
    try:
        cursor.execute("SELECT rowid, * from main")
        data = cursor.fetchall()
        conn_data = fzf.prompt(data)[0].translate(str.maketrans({"(": "", ")": "", "'": "", " ": ""})).split(',')
        ssh_command = "ssh" + " " + conn_data[4] + "@" + conn_data[3]
        print("{} *> Executing {}'{}'{}".format(BOLD, OKCYAN, ssh_command, ENDC))
        os.system(ssh_command)
    except:
        print('{} *> {}connection request terminated{}'.format(BOLD, WARNING, ENDC))


def list(cursor) -> str:
    header = column_header(cursor)
    header.insert(0, 'ID')
    separator = column_separator(header)
    cursor.execute("SELECT rowid, * from main")
    data = cursor.fetchall()
    pretty_print(data, header, separator)


def delete(cursor):
    print(" *> Enter the rowid's to drop in {}id1,id2{} format".format(BOLD, ENDC))
    d_inpt = input('INPUT: ').split(',')
    for row_id in d_inpt:
        cursor.execute('''DELETE from main WHERE rowid=? ''', (row_id,))
    print("{} *> '{}' drop(s) {}successful{}".format(BOLD, len(d_inpt), OKGREEN, ENDC))


def conn_close(connect, cursor):
    connect.commit()
    connect.close()


def main():
    try:
        sqlconn = initialize_db()
        (connect, cursor) = (sqlconn[0], sqlconn[1])
        args = [key for key, value in vars(parse_args()).items() if value]
        if len(args) > 0:
            globals()[args[0]](cursor)
        else:
            print("{} *> Use \'-h\' for options{}".format(BOLD, ENDC))
    except KeyboardInterrupt:
        print('{}\n *> {}exit{}'.format(BOLD, FAIL, ENDC))
        sys.exit(1)
    conn_close(connect, cursor)


if __name__ == "__main__":
    main()
