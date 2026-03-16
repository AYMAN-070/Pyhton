# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    construct.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/02 17:03:13 by ayhammou          #+#    #+#             #
#    Updated: 2026/02/02 17:17:19 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
import os
import site


def matrix_status() -> bool:
    """detect if user is on VENV"""
    return sys.prefix != sys.base_prefix


def environment_info() -> None:
    """Show environment informations"""
    try:
        in_venv = matrix_status()
        exe = sys.executable
        if in_venv:
            print("MATRIX STATUS: Welcome to the construct")
            print()
            print("Current Python: ", exe)
            print("Virtual Environment: ", os.path.basename(sys.prefix))
            print("Environment Path: ", sys.prefix)
            print()
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting the global"
                  "system.")
            print()
            print("Package installation path:")
            path = site.getsitepackages()
            if len(path) > 0:
                print(path[0])
            else:
                print("Unknown path")
        else:
            print("MATRIX STATUS: You're still plugged in")
            print()
            print("Current Python: ", exe)
            print("Virtual Environment: None detected")
            print()
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print()
            print("To enter the construct, run:\n"
                  "python -m venv matrix_env\n"
                  "source matrix_env/bin/activate # On Unix\n"
                  "matrix_env\n"
                  "Scripts\n"
                  "activate # On Windows\n"
                  "\n"
                  "Then run this program again.")
    except Exception as e:
        print("ERROR: ", e)


if __name__ == "__main__":
    environment_info()
