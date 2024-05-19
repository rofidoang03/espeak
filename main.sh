#!/bin/bash

# Pastikan Anda memiliki aircrack-ng dan tshark terinstal di sistem Anda.
# sudo apt-get install aircrack-ng tshark

if [ -z "$1" ]; then
    echo "Usage: $0 <capture-file.cap>"
    exit 1
fi

CAPFILE=$1

# Gunakan tshark untuk memindai file capture dan mencari paket EAPOL
# Filter: eapol
# Kolom yang diekstrak: bssid, frame.number
tshark -r "$CAPFILE" -Y "eapol" -T fields -e wlan.bssid -e frame.number | sort | uniq -c | awk '$1 == 4 {print $2}' > bssid_list.txt

if [ -s bssid_list.txt ]; then
    echo "BSSID with 4 EAPOL packets found:"
    cat bssid_list.txt
else
    echo "No BSSID found with 4 EAPOL packets."
fi

# Opsional: Hapus file sementara
# rm -f bssid_list.txt
