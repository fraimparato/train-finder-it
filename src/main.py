import sys
import tfi


def parse_args(args):
    if len(args) == 0:
        print("""No argument found, rerun this program with '-h' or '--help' \
to see which options you have""")
        exit(1)

    if args[0] == "--help" or args[0] == "-h":
        tfi.help()
    elif args[0] == "--search-solution" or args[0] == "-s":
        tfi.search_solution()
    elif args[0] == "--is-present" or args[0] == "-p":
        tfi.is_present()
    else:
        print("""Wrong first argument, rerun this program with '-h' or \
'--help' to see which options you have""")
        exit(1)


def main():
    args = sys.argv[1:]
    parse_args(args)


if __name__ == '__main__':
    main()
