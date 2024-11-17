from flask import Flask, request, render_template_string
from locotoml import LocoTOML

app = Flask(__name__)

# Create a LocoTOML object with the locale directory and the fallback locale
loc = LocoTOML(locale="ja", fallback_locale="en", locale_dir="loc")

@app.route('/')
def index():
    # Get the 'lang' query parameter from the request, default to 'ja'
    lang = request.args.get('lang', 'ja')
    loc.change_locale(lang)

    # Get the title, description, and h1 text from the TOML file
    title = loc.content.title()
    description = loc.content.description()
    h1_text = loc.content.h1()

    # Render the template with the title, h1 text, and description
    template = """
    <html>
        <head><title>{{ title }}</title></head>
        <body>
            <h1>{{ h1_text }}</h1>
            <p>{{ description }}</p>
        </body>
    </html>
    """
    return render_template_string(template, title=title, h1_text=h1_text, description=description)

if __name__ == '__main__':
    app.run(debug=True)