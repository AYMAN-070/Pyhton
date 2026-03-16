# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_stream_management.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/05 16:31:29 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/06 12:42:52 by ayhammou         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

import sys


def manage_streams() -> None:
    """Accesses the three sacred data channels: stdin, stdout, and stderr.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    ids: str = input("Input Stream active. Enter archivist ID: ")
    status: str = input("Input Stream active. Enter status report: ")
    print(f"[STANDARD] Archive status from {ids}: {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()
