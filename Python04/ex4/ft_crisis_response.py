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

def crisis_handler(filename: str) -> None:
    """Handles archive operations and manages failures gracefully.
    """
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ACCESS: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ''{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, anomaly contained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
