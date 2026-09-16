from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Video Downloader - Download Reels & Videos HD</title>
    <meta name="description" content="इंस्टाग्राम रील्स और वीडियो मुफ्त में फुल HD में डाउनलोड करें। बिना किसी ऐप या लॉगिन के सिर्फ लिंक पेस्ट करें और सीधी गैलरी में सेव करें। तेज़ और सुरक्षित!">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #f0f2f5; margin: 0; padding: 15px; box-sizing: border-box; }
        .box { background: #fff; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        h1 { font-size: 22px; color: #333; margin-bottom: 20px; }
        input[type="text"] { width: 100%; padding: 12px; margin: 12px 0; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; font-size: 15px; outline: none; }
        button { background: #0095f6; color: white; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; font-size: 16px; transition: 0.3s; }
        button:hover { background: #007bb5; }
        .result { margin-top: 20px; padding: 15px; background: #e8f5e9; border-radius: 8px; }
        a.dl-btn { display: inline-block; margin-top: 10px; background: #28a745; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; }
        .error { color: #d32f2f; margin-top: 15px; background: #ffebee; padding: 10px; border-radius: 6px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Insta Video Downloader</h1>
        <form method="post">
            <input type="text" name="url" placeholder="Instagram Reel / Video Link डालें" required>
            <button type="submit">Download Link निकालें</button>
        </form>
        {% if direct_url %}
        <div class="result">
            <p>✅ लिंक तैयार है!</p>
            <a href="{{ direct_url }}" class="dl-btn" target="_blank" download>वीडियो डाउनलोड करें</a>
        </div>
        {% elif error %}
        <div class="error"><p>❌ एरर: लिंक चेक करें या दोबारा कोशिश करें</p></div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    direct_url, error = None, None
    if request.method == "POST":
        url = request.form.get("url")
        ydl_opts = {'format': 'best', 'quiet': True, 'no_warnings': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                direct_url = info.get('url')
        except Exception as e:
            error = str(e)
    return render_template_string(HTML_CONTENT, direct_url=direct_url, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
  
