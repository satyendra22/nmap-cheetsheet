**A collection of useful Nmap commands**

## Verbose service/OS scan

```Bash
nmap -p 0-65535 -T4 -A -v [host/IP]
```

## Update scripts
```Bash
nmap --script-updatedb
```

## Default script scan
```Bash
nmap -sC -sV -oA nmap/out [host/IP]
```

## Banner grabbing
```Bash
nmap -sS -sV -p [Port number] -v -n -Pn --script banner [host/IP]
```

## Vulnerability scanning
```Bash
nmap -sV --script=exploit,external,vuln,auth,default -oX nmap-output.xml --webxml [host/IP]
```
