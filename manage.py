#!/usr/bin/env python3
import os
import sys
import getopt
import glob

def generate_templates():
    """Generates jinja2 files with the expected gettext syntax from txt files.
    """

    for f_in_path in glob.glob('**/*.txt'):
        f_out_path = os.path.splitext(f_in_path)[0] + '.jinja2'
        with open(f_in_path, 'r', encoding='utf-8') as f_in, \
                open(f_out_path, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                clean_line = line.strip()
                if len(clean_line):
                    print('{{ _(\'' + clean_line + '\') }}\n', file=f_out)

def usage():
    print("Usage: ./manage.py [command]")
    print()
    print("Commands:")
    print("-h --help\t- This help message")
    print("gentemplates\t- Generate jinja2 files with the expected gettext "\
            "from txt files")

def main():
    if len(sys.argv[1:]):
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'h', ['gentemplates'])
        except getopt.GetoptError as err:
            print(str(err))
            usage()
            sys.exit(2)

        for o, a in opts:
            if o in ('-h', '--help'):
                usage()
            if o in ('--gentemplates'):
                generate_templates()
    else:
        usage()

if __name__ == '__main__':
    main()
