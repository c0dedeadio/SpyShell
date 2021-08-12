# SpyShell

Interfacing with webshells using Curl or Burp Repeater is tedious and error-prone. Simplify your life with SpyShell, a simple webshell front-end written in Python.

## Features
 
- Full shell history with Ctrl-R search using GNU readline
- Automatic `stderr` redirection to `stdout`

## Example Usage

Use a webshell with the "command" parameter named `command`:
`spyshell -u https://targethost/webshell.php -c command`

Interface with shell using a nicer shell prompt:
`spyshell -u http://10.0.10.126/shell.php --pretty-prompt`
