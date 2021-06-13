s = "1" + "0"*80
print(s)

while "10" in s or "1" in s:
	if "10" in s:
		s = s.replace("10", "001")
	else:
		s = s.replace("1", "000")
print(len(s))