#!/bin/bash

# Pastikan Anda memiliki aircrack-ng dan tshark terinstal di sistem Anda.
# sudo apt-get install aircrack-ng tshark

if [ -z "$1" ]; then
    echo "Usage: $0 <capture-file.cap>"
    exit 1
fi

CAPFILE=$1

# Perbaiki file capture yang mungkin rusak menggunakan editcap
TEMP_CAPFILE=$(mktemp /tmp/fixed_capture.XXXXXX.cap)
editcap -F libpcap "$CAPFILE" "$TEMP_CAPFILE"

# Gunakan tshark untuk memindai file capture yang telah diperbaiki dan mencari paket EAPOL
# Filter: eapol
# Kolom yang diekstrak: bssid, frame.number
tshark -r "$TEMP_CAPFILE" -Y "eapol" -T fields -e wlan.bssid -e frame.number | sort | uniq -c | awk '$1 == 4 {print $2}' > bssid_list.txt

if [ -s bssid_list.txt ]; then
    echo "BSSID with 4 EAPOL packets found:"
    cat bssid_list.txt
else
    echo "No BSSID found with 4 EAPOL packets."
fi

# Hapus file sementara
rm -f "$TEMP_CAPFILE" bssid_list.txt
