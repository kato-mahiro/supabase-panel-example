import panel as pn
from app.utils.supabase import supabase

def create_login_page():
    email_input = pn.widgets.TextInput(name='メールアドレス', placeholder='email@example.com')
    password_input = pn.widgets.PasswordInput(name='パスワード', placeholder='パスワードを入力')
    login_button = pn.widgets.Button(name='ログイン', button_type='primary')
    message = pn.pane.Str('')

    def handle_login(event):
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email_input.value,
                "password": password_input.value
            })
            message.object = "ログインに成功しました！"
            return response
        except Exception as e:
            message.object = f"ログインに失敗しました: {str(e)}"
            return None

    login_button.on_click(handle_login)

    return pn.Column(
        pn.pane.Markdown('# ログイン'),
        email_input,
        password_input,
        login_button,
        message
    )