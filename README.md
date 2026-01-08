How to run this program? Just copy this command 
```bash
python3 Nmap.py
```

if you find this "Add custom Nmap options (space-separated):" in the custom menu in Nmap, just fill in with this prompt

1. **Port and service scanning**:
   - `-p-`: Scan all ports (default).
   - `-p 80,443`: Scan specific ports.
   - `-sS`: TCP SYN scan (stealth).
   - `-sU`: UDP scan.
   - `-sV`: Service version detection.
   - `-sC`: Run default Nmap scripts.

2. **Operating system detection**:
   - `-O`: OS detection.
   - `--osscan-guess`: Guess OS if uncertain.

3. **Execution timing settings**:
   - `-T0-T5`: Set execution speed (paranoid-insane).
   - `-T3`: Normal timing.

4. **Additional Nmap scripts**:
   - `--script=exploit`: Run exploitation scripts.
   - `--script=discovery`: Run discovery scripts.
   - `--script=vuln`: Run vulnerability detection scripts.

5. **Output and logs**:
   - `-oX`: Save results in XML.
   - `-oN`: Save results in plain text.
   - `-oG`: Save results in greppable format.

6. **Miscellaneous**:
   - `-Pn`: Disable host ping.
   - `-f`: Packet fragmentation.
   - `-v`: Verbose mode.
   - `-n`: Disable DNS resolution.

example of use:
Add custom Nmap options (space-separated): -Pn
