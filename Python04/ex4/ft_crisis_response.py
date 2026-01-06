# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_crisis_response.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/06 11:24:39 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/06 12:50:09 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as file:
            print("ESPONSE: Archive found in storage matrix")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print()
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        raise PermissionError
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print()
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ''{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Security protocols deny access")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
