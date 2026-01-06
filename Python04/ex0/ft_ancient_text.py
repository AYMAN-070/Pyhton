# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_ancient_text.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/05 11:05:24 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/06 12:39:33 by ayhammou         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        content = file.read()
        print(content)
        file.close()
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
