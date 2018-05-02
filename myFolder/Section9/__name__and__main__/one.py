# one.py

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE")

if __name__ == '__main__':
	print('ONE.PY is beign run directly!')
else:
	print('ONE.PY has been imported!')
