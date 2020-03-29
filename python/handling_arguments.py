#!/usr/bin/env python3

"""
MySoftware: A fake python3 script.
by Paolo Niccolò Giubelli <paoloniccolo.giubelli@gmail.com>

How to parse arguments in a Python CLI script?
In the following code I put some useful, self-explanatory
examples using the argparse library, which is good and is
included in the standard library.

Please notice how this library handles everything out of the box.
"""

import argparse

module_name = "MySoftware"
version = "1.0 build 0x00000001"
listen_port = 1234
service_name = ""

def main():
    global listen_port, service_name
    # Initialize the parser, using a formatter class and some info
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=f"{module_name} v.{version}")
    # This is an optional argument (short and long version).
    # store_true means that is a boolean argument, accepting no value
    # help sets the help message for the argument
    parser.add_argument("-v","--version",
                        help="Show current version and exit",
                        action="store_true")
    # This is also an optional argument (short and long version).
    # This needs a value that must be and integer. That's why I set type=int
    parser.add_argument("-p","--port",
                        help="Listen on this port",
                        type=int)
    # This is a mandatory, **positional** argument. It needs a value.
    parser.add_argument("service_name",
                        help="The service name")
    
    # Parses the arguments and fills in the data
    args = parser.parse_args()

    # Check if --version is set
    if args.version:
        print(f"{module_name} v.{version}")

    # Note: I set type=int, so the argument is automatically
    # converted to an integer value.
    if args.port:
        if args.port >=0 and args.port < 65536:
            listen_port = args.port
        else:
            print(f"Port {args.port} is out of valid range. Using default {listen_port}")
    
    # Any argument is a string by default, unless I set type=
    service_name = args.service_name

    print(f"{service_name} executing...")
    print(f"Listening on localhost:{listen_port}")

if __name__ == "__main__":
    main()