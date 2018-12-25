**Docker Container**

This is a Docker Container that houses several useful Pentesting tools and Utilities including:
Metasploit, Netcat, Nmap, Enum4Linux

This is intended to act as a lighweight pentesting toolset. This is super barebones but will be adding additional scripts & utilities as time goes on!

**Usage (Guide)**

1) Launch the Docker file after pulling it.
```bash
docker run --interactive --tty td4b/pentools:latest
```
2) You will be initially started in the MSF console shell. You may call Bash to access the other Pentesting tools via.
```bash
msf5 > bash
[*] exec: bash
bash-4.4$ 
```
3) Back to msf console.
```bash
bash-4.4$ exit
exit
msf5 > 
```

That's it, enjoy :)
