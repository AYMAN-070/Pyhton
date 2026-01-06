# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_archive_creation.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/05 16:02:25 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/06 12:41:05 by ayhammou         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...")
    print()
    file = open("new_discovery.txt", "w")
    file.write("[ ENTRY 001 ] New quantum algorithm discovered\n")
    file.write("[ ENTRY 002 ] Efficiency increased by 347%\n")
    file.write("[ ENTRY 003 ] Archived by Data Archivist trainee\n")
    file.close()
    print("Inscribing preservation data...")
    file1 = open("new_discovery.txt", "r")
    content = file1.read()
    print(content)
    print()
    print("Data inscription complete. Storage unit sealed")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
    file1.close()
