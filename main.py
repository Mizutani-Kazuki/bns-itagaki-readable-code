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


def output_user_and_words(words_list, user_name, id=None):
    """
    取得した単語情報の出力
    
    Parameters
    ----------
    words_list: str
        CSVファイルのPath
    user_name: str
        ユーザー名
    id: int (default None)
        単語ID
    """
    print("ユーザー名:", user_name)
    for index, word_info in enumerate(words_list):
        # リストの添え字+1をIDとして出力する
        current_id = index + 1
        if id: # 引数が0のときはすべての単語情報を出力
            if current_id == id:
                print(current_id, ': ', word_info[0], sep='')
        else: # 引数が0以外のときは一致するIDの単語のみ出力
            print(current_id, ': ', word_info[0], sep='')


def check_args(args):
    """
    コマンドから必要な情報を抜き出す関数

    Parameters
    ----------
    args: str
        コマンドで入力された引数
    Returns
    -------
    ユーザー名と単語IDを出力する。単語IDが入力されていなければユーザー名だけ出力
    """
    if len(args) >= 3:
        return args[1], int(args[2])
    else:
        return args[1], None


def main(args):
    """
    単語情報の出力
    入力ファイルから単語情報を読み込んでターミナル上に出力

    Parameters
    ----------
    args: str
        コマンドで入力された引数
    """
    user_name, word_id = check_args(args)
    words_list = make_word_list(INPUT_DICTIONARY_DATA_PATH)
    output_user_and_words(words_list, user_name, word_id)


if __name__ == '__main__':
    """
    main関数の実行
    """
    args = sys.argv # コマンドライン引数を取得
    main(args)
