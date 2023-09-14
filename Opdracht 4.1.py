my_list = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018", "Fortnite Battle Royale 39 Million 2017", "Apex Legends 50 Million (1 Month) 2019", "Leauge of Legends (LOL) 27 Million 2009", "Counter Strike; Global Offensive 32 Million 2014", "Heartstone 29 Million 20120", "Minecraft 91 Million 2011", "DOTA 2 5 million 2015", "The Division 2 N/A 2019", "The Splatoon 2"]

print(my_list[4])

print(len(my_list[7]))

print(f"Er zitten: {len(my_list)} games in de lijst.")

my_list.insert(1, "Snake")
print(my_list)

print(f"Helaas heeft de game {my_list[-1]} het niet gered om in de top 10 te blijven.\n"
      f"We nemen waardig afscheid van {my_list[-1]}.")
my_list.remove("The Splatoon 2")
print(my_list)

my_list.remove(my_list[6])
my_list.insert(6, "Heartstone 29 miljoen 2012")
print(my_list)