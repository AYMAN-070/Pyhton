# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_sacred_scroll.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/13 15:51:12 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/13 15:51:14 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

if __name__ == "__main__":
    import alchemy.elements
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ",
          alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ",
          alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ",
          alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ",
          alchemy.elements.create_air())
    print()
    import alchemy
    print("Testing package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): ", alchemy.create_fire())
    print("alchemy.create_water(): ", alchemy.create_water())
    try:
        print("alchemy.create_earth(): ", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()
    print("Package metadata:")
    try:
        print("Version: ", alchemy.__version__)
        print("Author: ", alchemy.__author__)
    except Exception:
        print("Metadata missing...")
