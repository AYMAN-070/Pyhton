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

def create_archive(filename: str) -> None:
    """Establishes a new preservation protocol by creating fresh archive
    entries."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successfully...")
    print()
    try:
        with open(filename, "w") as vault:
            print("Storage unit created successfully...")
            print("Inscribing preservation data...")
            entries = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
                ]
            for entry in entries:
                vault.write(entry + "\n")
                print(entry)
        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: Access denied. Security protocols prevent writing here.")


if __name__ == "__main__":
    create_archive("new_discovery.txt")
