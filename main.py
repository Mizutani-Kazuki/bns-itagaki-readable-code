# 入力ファイルのパス
INPUT_DICTIONARY_DATA_PATH = "./dictionary-data.csv"


def main():
    """
    単語情報の出力
    入力ファイルから単語情報を読み込んでターミナル上に出力
    """
    words_list = [] # 単語情報を保持するリスト

    # 入力ファイルを開く
    with open(INPUT_DICTIONARY_DATA_PATH, encoding='utf-8') as input_file:
        # 入力ファイルのテキストを1行ずつrowに格納して処理
        for row in input_file:
            # 入力ファイルはcsvを想定しているので','区切りで取り出す
            word_info = row.strip().split(',')
            # 入力ファイルから読み込んだ単語をリストに格納
            words_list.append(word_info)

    # 取得した単語情報の出力
    for index, word_info in enumerate(words_list):
        # リストの添え字+1をIDとして出力する
        print(index + 1, ': ', word_info[0], sep='')


if __name__ == '__main__':
    """
    main関数の実行
    """
    main()