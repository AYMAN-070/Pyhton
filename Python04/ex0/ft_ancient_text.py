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

def recover_ancient_text(filename: str) -> None:
    """
    Recover data from the ancient storage vault.
    Type hints included as per Protocol V.2.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault:", filename)
    try:
        with open(filename, "r") as file:
            print("Connection established...")
            print()
            print("RECOVERED DATA:")
            content = file.read()
            print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
