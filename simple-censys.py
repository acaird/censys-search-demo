#!/usr/bin/env python
import censys.ipv4
import os
import socket

UID = os.getenv("CENSYS_API_ID")
KEY = os.getenv("CENSYS_KEY")
if UID is None or KEY is None:
    print(
        "Please set both CENSYS_API_ID and "
        "CENSYS_KEY environment variables"
    )
    exit(1)

domains = censys.ipv4.CensysIPv4(UID, KEY)
domain = "ncmich.edu"

for w in domains.search(domain):
    hostname = socket.gethostbyaddr(w["ip"])[0]
    print(
        f"{hostname:25s} | {w['ip']:>15s} | "
        f"{w['location.city']:>20s} | {w['protocols']}"
    )
