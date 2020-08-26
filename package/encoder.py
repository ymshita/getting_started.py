import base64
import sys

def str_to_base64(x):
    """文字列をbase64表現に変換する
    b64encode()はbytes-like objectを引数にとるため
    文字列はencode()でbytes型にして渡す
    """
    return base64.b64encode(x.encode('utf-8'))

def main():
    if len(sys.argv) > 1:
        target = sys.argv[1] #python3コマンドの引数を処理　python3 encoder.py book であれば、sys.argvは [encoder.py, book]
        print(str_to_base64(target))
    else:
        raise ValueError('引数がありません')


print('__name__: ',__name__)
if __name__ == '__main__': #モジュールをスクリプトとして使いたいときに記述するイディオム. メインモジュールかどうか判定
    main()

__all__ = ['str_to_base64']
