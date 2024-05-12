import flet as ft
import encrypt  # encrypt.pyファイルから関数をインポート

def main(page: ft.Page):
    page.title = "Text Encryption App"
    
    # 入力フィールド
    input_field = ft.TextField(label="Enter text to encrypt", width=300)
    
    # 暗号化されたテキストを表示するフィールド
    encrypted_text_area = ft.TextField(label="Encrypted Text", multiline=True, width=300, height=100)
    
    # 使用した鍵を表示するフィールド
    key_text_area = ft.TextField(label="Encryption Key", multiline=True, width=300, height=100)
    
    # 暗号化ボタン
    encrypt_button = ft.ElevatedButton(text="Encrypt")
    
    def on_encrypt_click(e):
        # 入力されたテキストを取得し暗号化
        plain_text = input_field.value
        encrypted_text, key_text = encrypt.encrypt_text(plain_text)
        
        # 結果をテキストフィールドに設定
        encrypted_text_area.value = encrypted_text
        key_text_area.value = key_text
        page.update()

    encrypt_button.on_click = on_encrypt_click
    
    # ページにウィジェットを追加
    page.add(input_field, encrypt_button, encrypted_text_area, key_text_area)

if __name__ == "__main__":
    ft.app(target=main)
