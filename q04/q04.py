"""
　長さ n[cm]の１本の棒を１[cm]単位に切り分けることを考えます。
ただし、１本の棒を一度に切ることができるのは１人だけです。
切り分けられたぼうが３本あれば、同時に３人で切ることができます。
　最大 m人の人がいる時、最短何回で切り分けられるかを求めて下さい。
例えば、 n = 8,  m = 3 の時は４回で切り分けることができます。

問題 1:
n = 20,  m = 3 のときの回数を求めてください。

問題 2:
n = 100,  m = 5 のときの回数を求めてください。
"""

from typing import List

def solve_q04(n: int, m:int):
	"""
	Args:
		n :int 棒の長さ
		m :int 人数
	Returns:
		None
	"""
	length = n # 棒の長さ
	people_num = m # 人数
	count = 0 # かかった回数

	# 棒の長さのリスト
	bars = [length]

	def cut(bars: List[int], num_people: int):
		""" 棒の中で長さが最大のものを２分割する """
		nonlocal count

		# 棒の数と人数で少ない方の数だけ１度に処理する
		for _ in range(min(len(bars), num_people)):
			# 棒のリストの中で長さが最大のものを取り出す
			idx = bars.index(max(bars))
			l = bars.pop(idx)

			# 取り出した棒を半分に切り分けて、リストに追加
			# 偶数の場合
			if l % 2 == 0:
				bars.append(l/2)
				bars.append(l/2)
			# 奇数の場合
			else:
				left = int(l/2)
				right = l - left
				bars.append(left)
				bars.append(right)
		count += 1
		return bars


	# 全て１になるまで実行
	while len(bars) < length:
		bars = cut(bars, people_num)

	# 答え
	print(f'{n}cm {m}人 の場合 {count}回')



if __name__ == "__main__":
	solve_q04(n=8,  m=3)
	solve_q04(n=20,  m=3)
	solve_q04(n=100, m=5)