"""
    １ ~ 100までの番号が書かれた100枚のカードが順番に並べられています。
最初、全てのカードは裏返しの状態で置かれています。
ある人が２番目のカードから、１枚おきにカードを裏返していきます。
すると、2、4、6...100番目のカードが表を向くようになります。

    次に別の人が、３番目のカードから２マイおきにカードを裏返していきます
（裏向きのカードは表を向き、表を向いているカードは裏返されます）。
また、別の人が４番目のかーだから３枚おきにカードを裏返していきます。

    このようにn番目のカードから n-1枚おきにカードを裏返す操作を
どのカードの向きも変わらなくなるまで続けたとします。

問題:
カードの向きが変わらなくなった時、裏向きになっているカードの番号を全て求めて下さい。

"""


def solve_q03():
    num = 2

    # (表)True / (裏)False
    # カードの枚数分表と裏を表すリストを作成
    cards = [False] * 100

    # カードの向きが変わらなくなるのは101番目から
    # よって、100までを実行する
    while num < 101:
        for idx, is_obverse in enumerate(cards):
            # カードに書かれた数字
            number = idx + 1

            if number % num == 0:
                cards[idx] = not is_obverse
        num += 1

    # 裏向きのカードのリスト
    reverse_card_list = []

    # カードの表裏を全て確認し、裏向きのカードの数をリストに追加
    for idx, is_obverse in enumerate(cards):
        if not is_obverse:
            number = idx + 1
            reverse_card_list.append(number)

    return reverse_card_list


if __name__ == '__main__':
    answer = solve_q03()
    print(answer)

