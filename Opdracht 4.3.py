telefoonnummers = {"The Simpsons": "636-555-3226",
"Vegas Vacation": "555-0100",
"Ghostbusters": "555-23678",
"Billy Madison": "555-0840",
"Swingers": "213-555-4679",
"Bruce Almighty": "555-0123",
"Seinfeld": "555-FILK",
"Arrested Development": "555-0113",
"Die Hard With a Vengeance": "555-0001",
"The A-Team": "555-6162"}
print(telefoonnummers)
print()

# A
print(f"Het telefoonnummer van Bruce Almighty is {telefoonnummers['Bruce Almighty']}")
print(telefoonnummers)
print()

# B
telefoonnummers["Harry Potter"] = "605-475-6961"
print(telefoonnummers)
print()

# C
old_phone_number = telefoonnummers["Ghostbusters"]
new_phone_number = "555-2368"
print(f"Het telefoonnummer {old_phone_number} van Ghostbusters is gewijzigd naar {new_phone_number}.")
print(telefoonnummers)
print()

# D
print(f"Telefoonnummer {telefoonnummers['Seinfeld']} van Seinfeld is verwijderd")
del telefoonnummers["Seinfeld"]
print(telefoonnummers)
print()

# E
print(f"In de dictionary zitten {len(telefoonnummers)} telefoonnummers.")
print(telefoonnummers)
print()
