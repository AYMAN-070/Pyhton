# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 14:31:15 by ayhammou          #+#    #+#              #
#    Updated: 2025/12/23 15:41:47 by ayhammou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PLant:
	def __init__(self, name, height):
		self.name = name
		self.height = height
	def grow(self, cm):
		self.height = self.height + cm
		print(f"{self.name}: grew {cm}cm")
	def info(self)
		print(f"{self.name}: {self.height}cm")
class FowringPlant(PLant):
	def __init__(self, name, height, blooming = True):
		super().__init__(name, height)
		self.blooming = blooming
	def info(self):
		status = "bloomig" if self.bloomig else "not blooming"
		return f"{self.name}: {self.height}cm, {status}"
class PrizeFlower(FowringPlant):
	def __init__(self, name, height, points):
		super().__init__(name, height, bloomig = True)
		self.points = points
	def info(self)
		return f"{self.name}: {self.height}cm, bloomig, Prize points: {self.points}"
