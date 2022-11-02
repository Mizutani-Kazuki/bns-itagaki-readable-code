# 入力ファイルのパス
INPUT_DICTIONARY_DATA_PATH = "./dictionary-data.csv"


def main():
    """
    単語情報の出力
    入力ファイルから単語情報を読み込んでターミナル上に出力
    """
    # 入力ファイルを開く
    with open(INPUT_DICTIONARY_DATA_PATH, encoding='utf-8') as input_file:
        # 入力ファイルのテキストを1行ずつrowに格納して処理
        for row in input_file:
            # 入力ファイルはcsvを想定しているので','区切りで取り出す
            word_list = row.split(',')
            # 入力ファイルから読み込んだ単語を画面に出力
            print(word_list[0])


if __name__ == '__main__':
    """
    main関数の実行
    """
    main()