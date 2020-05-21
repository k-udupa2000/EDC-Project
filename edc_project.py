l = ["abcefgz","abcdzjm","adef","abcdjm","adefgz","aefgz",
	"acdefz","bcefgz","adjm","bcde","efgkl",
	"def","bcefhk","bcefhl","abcdef","abefgz",
	"abcdefl","abefgzl","acdfgz","ajm","bcdef",
	"efkn","bcefln","hkln","hkm","adkn"]

ascii = [106,104,102,103,101,110,100,109,97,107,98,122,121,99,108]

def return_encode(i):
	r = ""
	for x in range(15):
		if chr(ascii[x]) in l[i]:
			r+="1" 
		else:
			r+="0"
	return r
print("Enter the four characters in all CAPS Sample input = ABCD")
s = input()
ll = {}
for i in range(len(s)):
	a = return_encode(ord(s[i])-65)
	ll[i] = a
	print(a)
print("In the following lines each line represents a particular bit value of all characters.")
for i in range(15):
	print("Bit number {}" .format(i+1), end=' ')
	for keys in ll:
		print(ll[keys][i], end='')
	print()