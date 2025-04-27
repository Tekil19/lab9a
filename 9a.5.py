faculty = ["Darshit", "Mukesh", "Punit", "Prakash", "Sivaraman"]

filt = [name for name in faculty if len(name) <= 8]

print("Filtered Names:", filt)
