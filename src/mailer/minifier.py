import htmlmin

try:
    input_html = '''
    <body   style="background-color: tomato;">
    <h1>  htmlmin   rocks</h1>
    <pre>
        and rolls
    </pre>
    </body>'''

    minified = htmlmin.minify(input_html)
    print(minified)
except SyntaxError as e:
    print(e)