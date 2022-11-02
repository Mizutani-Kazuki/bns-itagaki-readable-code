import sys


# 入力ファイルのパス
INPUT_DICTIONARY_DATA_PATH = "./dictionary-data.csv"

def make_word_list(file_path):
    """
    csvファイルから単語情報を読み出し、リストに格納する
    
    Parameters
    ----------
    file_path: str
        CSVファイルのPath
    Returns
    -------
    words_list: list
        単語が格納されているリスト
    """
    words_list = [] # 単語情報を保持するリスト
    with open(file_path, encoding='utf-8') as input_file:
        # 入力ファイルのテキストを1行ずつrowに格納して処理
        for row in input_file:
            # 入力ファイルはcsvを想定しているので','区切りで取り出す
            word_info = row.strip().split(',')
            # 入力ファイルから読み込んだ単語と読み仮名をリストに格納
            words_list.append(word_info)

    return words_list


def output_words(words_list, id=None):
    """
    取得した単語情報の出力
    
    Parameters
    ----------
    words_list: str
        CSVファイルのPath
    id: int (default None)
        単語ID
    """
    for index, word_info in enumerate(words_list):
        current_id = index + 1
        if id <= 0: # 引数が0のときはすべての単語情報を出力
            # リストの添え字+1をIDとして出力する
            print(current_id, ': ', word_info[0], sep='')
        else: # 引数が0以外のときは一致するIDの単語のみ出力
            if current_id == id:
                print(current_id, ': ', word_info[0], sep='')


def main(target_id=None):
    """
    単語情報の出力
    入力ファイルから単語情報を読み込んでターミナル上に出力
    """
    words_list = make_word_list(INPUT_DICTIONARY_DATA_PATH)

    # 取得した単語情報の出力
    for index, word_info in enumerate(words_list):
        # リストの添え字+1をIDとして出力する
        current_id = index + 1
        if target_id: # 引数が0のときはすべての単語情報を出力
            if current_id == target_id:
                print(current_id, ': ', word_info[0], sep='')
        else: # 引数が0以外のときは一致するIDの単語のみ出力
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
        main()