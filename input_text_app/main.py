import flet as ft

def main(page: ft.Page):
    input_field = ft.TextField(label="Please input sentence")
    result_text = ft.Text("")  # 結果を表示するTextウィジェット
    
    async def dismiss_dialog(e):
        cupertino_alert_dialog.open = False
        await page.update_async()
        
        if e.control.text == "OK":
            # 何かの処理をここで行う（例：入力されたテキストをそのまま表示）
            encrypted_text = "Encrypted: " + input_field.value  # ここで暗号化処理を想定
            result_text.value = encrypted_text  # 結果のTextウィジェットを更新
            await page.update_async()

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("暗号化を開始します"),
        content=ft.Text("実行して良いですか？"),
        actions=[
            ft.CupertinoDialogAction(text="OK", is_destructive_action=True, on_click=dismiss_dialog),
            ft.CupertinoDialogAction(text="Cancel", on_click=dismiss_dialog),
        ],
    )

    def open_dlg(e):
        cupertino_alert_dialog.open = True
        page.dialog = cupertino_alert_dialog
        page.update()

    # UI要素をページに追加
    page.add(ft.SafeArea(ft.Text("Enter the sentence you want to encrypt!")))
    page.add(input_field)
    page.add(ft.ElevatedButton("暗号化開始！", on_click=open_dlg))
    page.add(result_text)  # 結果を表示するTextをページに追加

if __name__ == "__main__":
    ft.app(target=main)
