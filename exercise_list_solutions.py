# %% [markdown]
# 3.4 - Guest List

# %%
guest_list = ["Arshad", "Manahil", "Madi", "Mahrukh", "Kiran"]
message = "Dear {}, you are invited to my graduation party."
for guest in guest_list:
    print(message.format(guest))

# %% [markdown]
# 3.5 - Changing Guest List

# %%
guest_list = ["Arshad", "Manahil", "Madi", "Mahrukh", "Kiran"]
print(f"My apologies, {guest_list[4]} would not be able to show up at the party.")
guest_list[4] = "Georgie"
message = "You're invited to the party, {}"
for guest in guest_list:
    print(message.format(guest))

# %% [markdown]
# 3-6 More Guests

# %%
guest_list = ["Arshad", "Manahil", "Madi", "Mahrukh", "Kiran"]
guest_list[4] = "Georgie"
print("Good news! I found a bigger table!")

guest_list.insert(0, "Derik")
guest_list.insert(3, "Dana")
guest_list.append("Alan")

for guest in guest_list:
    print(f"Dear {guest}, you're invited to dinner!")

# %% [markdown]
# 3-7 Shrinking Guest List

# %%
guest_list = ["Arshad", "Manahil", "Madi", "Mahrukh", "Kiran"]
guest_list[4] = "Georgie"

print("I can only invite two people for dinner.")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Dear {removed_guest}, I'm so sorry, I can't invite you to dinner.")

for guest in guest_list:
    print(f"Dear {guest}, you're still invited to dinner!")

del guest_list[0]
del guest_list[0]
print(guest_list)  

# %% [markdown]
# 3-8 Seeing the World

# %%
places_to_visit = ["Kashmir", "Gilgit", "Hunza", "Spain", "Japan"]
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)


# %%
places_to_visit = ["Kashmir", "Gilgit", "Hunza", "Spain", "Japan"]
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)


# %%
places_to_visit = ["Kashmir", "Gilgit", "Hunza", "Spain", "Japan"]
sorted_list = places_to_visit.copy()
places_to_visit.sort()
print(places_to_visit)
print(sorted_list)

# %% [markdown]
# 3-9 Practicing Python Functions
# Using len()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
print(len(languages))



# %% [markdown]
# Using append()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.append("Russian")
print(languages)


# %% [markdown]
# Using insert()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.insert(0, "Swahili")
print(languages)

# %% [markdown]
# Using remove()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.remove("Punjabi")
print(languages)

# %% [markdown]
# Using pop()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.pop()
print(languages)

# %% [markdown]
# Using index()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
print(languages.index("Arabic"))


# %% [markdown]
# Using Count()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu", "French", "Dutch", "French", "Siraiki"]
print(languages.count("French"))

# %% [markdown]
# Using Sort()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.sort()
print(languages)

# %% [markdown]
# Using reverse()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.reverse()
print(languages)

# %% [markdown]
# Using extend()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
more_languages = ["English", "Hindi", "Chinese", "Cantonese"]
languages.extend(more_languages)
print(languages)

# %% [markdown]
# Using clear()

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
languages.clear()
print(languages)

# %% [markdown]
# Practicing Index Error: 3.10

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
print(languages[-10])

# %% [markdown]
# Index Error Correction:

# %%
languages = ["Espanol", "French", "Arabic", "Punjabi", "Urdu"]
print(languages[3])


