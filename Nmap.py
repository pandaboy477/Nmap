#!/usr/bin/env python3
import subprocess
import argparse
import json
import sys
import os
from datetime import datetime

class NmapScanner:
    def __init__(self):
        # Define scan profiles with specific options
        self.profiles = {
            'basic': {
                'desc': 'Basic scan (all ports, service version)',
                'options': ['-p-', '-sV', '--open']
            },
            'aggressive': {
                'desc': 'Aggressive scan (full port, OS detection)',
                'options': ['-A', '-T4', '-p-']
            },
            'light': {
                'desc': 'Light scan (TCP/UDP, fast)',
                'options': ['-sS', '-sU', '-T4', '-F']
            },
            'stealth': {
                'desc': 'Stealth scan (no ping, slow)',
                'options': ['-sS', '-Pn', '-T2', '-f']
            }
        }
        
        # Timing templates
        self.timing_templates = {
            '0': 'paranoid', '1': 'sneaky', '2': 'polite',
            '3': 'normal', '4': 'aggressive', '5': 'insane'
        }
        
        # Service detection
        self.service_detection = [
            '-sV',  # Version detection
            '-sC',  # Script scanning
            '-O'    # OS fingerprinting
        ]
        
        # Aggressive mode
        self.aggressive_mode = ['-A']

    def get_port_range(self):
        """Get custom port range from user"""
        prompt = "Enter port range (e.g., 1-1000, 80,443): "
        return input(prompt).strip() or '-p-'

    def get_timing_template(self):
        """Get timing template from user"""
        print("\nTiming templates:")
        for num, desc in self.timing_templates.items():
            print(f"  {num}. {desc}")
        choice = input("Select timing template (0-5): ").strip()
        return f"-T{choice}" if choice in self.timing_templates else "-T3"

    def build_options(self, profile_key, custom_options=None):
        """Build complete Nmap options"""
        if custom_options:
            return custom_options
        
        # Start with profile options
        options = self.profiles.get(profile_key, self.profiles['basic'])['options'].copy()
        
        # Add service detection if not already present
        if not any(opt.startswith('-s') for opt in options):
            options.extend(self.service_detection)
        
        return options

    def scan(self, target, options):
        """Execute Nmap scan"""
        cmd = ['nmap'] + options + [target]
        
        try:
            print(f"[*] Starting scan at {datetime.now()}")
            print(f"[*] Command: {' '.join(cmd)}")
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                self.display_results(stdout)
                return True
            else:
                print(f"[!] Scan failed: {stderr}")
                return False
                
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            return False

    def display_results(self, output):
        """Parse and display results"""
        lines = output.split('\n')
        results = {'ports': [], 'services': []}
        
        for line in lines:
            if "PORT" in line:
                results['ports'].append(line)
            elif "open" in line:
                results['services'].append(line.strip())
        
        # Print formatted results
        print("\n[+] Scan Results:")
        for port_line in results['ports']:
            print(f"  {port_line}")
        
        if results['services']:
            print("\n[+] Services Found:")
            for service in results['services']:
                print(f"  {service}")
        else:
            print("\n[!] No open services found.")

def main():
    scanner = NmapScanner()
    
    # Main menu
    menu = """
    Nmap Scanner
    1. Basic scan
    2. Aggressive scan
    3. Light scan
    4. Stealth scan
    5. Advanced scan (custom options)
    6. Exit
    """
    
    while True:
        print(menu)
        choice = input("Select scan type (1-6): ").strip()
        
        if choice == '6':
            print("[*] Exiting...")
            sys.exit(0)
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("[!] Invalid option")
            continue
            
        target = input("Enter target (domain/IP): ").strip()
        if not target:
            print("[!] Target required")
            continue
            
        # Build options based on choice
        if choice == '5':
            # Custom options
            options = []
            
            # Port range
            port_range = scanner.get_port_range()
            options.append(port_range)
            
            # Timing template
            timing = scanner.get_timing_template()
            options.append(timing)
            
            # Service detection
            detect_services = input("Enable service detection (Y/n): ").strip().lower()
            if detect_services != 'n':
                options.extend(scanner.service_detection)
            
            # Aggressive mode
            aggressive = input("Enable aggressive mode (Y/n): ").strip().lower()
            if aggressive != 'n':
                options.extend(scanner.aggressive_mode)
                
            # Additional options
            custom = input("Add custom Nmap options (space-separated): ").strip()
            if custom:
                options.extend(custom.split())
                
        else:
            # Use predefined profile
            options = scanner.build_options(choice)
            
        # Execute scan
        scanner.scan(target, options)

if __name__ == "__main__":
    main()