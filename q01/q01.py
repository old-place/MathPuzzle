

def find_palindromic_number() -> int:
	"""
	2進数、8進数、10進数のいずれで表現しても回文数となる数のうち
	10進数の10以上で最小の値を求める
	"""
	num = 11

	while True:

		# (文字列)
		bin_num = bin(num)[2:] # 2進数
		oct_num = oct(num)[2:] # 8進数
		dec_num = str(num) # 10進数

		if (bin_num == bin_num[::-1]) and \
			(oct_num == oct_num[::-1]) and (dec_num == dec_num[::-1]):
			return num

		# 1億過ぎても見つからない場合 -1 を返す
		if num > 10**8:
			return -1
		num += 2


if __name__ == '__main__':
	num = find_palindromic_number()
	if num < 0:
		print('NOT FOUND')
	else:
		print('2進数:  ',  bin(num)[2:])
		print('8進数:  ',  oct(num)[2:])
		print('10進数:  ', num)
