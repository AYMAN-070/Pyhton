# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_command_quest.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/28 11:56:33 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:36:19 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Program name: ", sys.argv[0])
        print("Total arguments: 1")
    if len(sys.argv) > 1:
        print("Program name: ", sys.argv[0])
        print("Arguments received: ", (len(sys.argv) - 1))
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print("Total arguments: ", len(sys.argv))
