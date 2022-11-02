import sys


# 入力ファイルのパス
INPUT_DICTIONARY_DATA_PATH = "./dictionary-data.csv"


def main(target_id):
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
        current_id = index + 1
        if target_id <= 0: # 引数が0のときはすべての単語情報を出力
            # リストの添え字+1をIDとして出力する
            print(current_id, ': ', word_info[0], sep='')
        else: # 引数が0以外のときは一致するIDの単語のみ出力
            if current_id == target_id:
                print(current_id, ': ', word_info[0], sep='')


if __name__ == '__main__':
    """
    main関数の実行
    """
    args = sys.argv # コマンドライン引数を取得
    if len(args) >= 2: # IDの指定がある場合
        if args[1].isdigit(): # IDが数字で入力されているかどうか判定
            main(int(args[1]))
    else: # IDの指定がない場合
        main(0)