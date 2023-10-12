import os

versions: list[str] = [
    '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23'
]

root_tpl = '''
<!doctype html>
<html lang=en>
<head>
    <meta charset=utf-8>
    <meta http-equiv=refresh content="0; url=https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/">
    <title>Redirecting to https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/</title>
</head>
<body>
    <h1>Redirecting to https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/</h1>
    <a href="https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/">Click here if you are not redirected.</a>
</body>
</html>
'''

onepage_tpl = '''
<!doctype html>
<html lang=en>
<head>
    <meta charset=utf-8>
    <meta http-equiv=refresh content="0; url=https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/reference/generated/kubernetes-api/v{{verdot}}/">
    <title>Redirecting to https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/reference/generated/kubernetes-api/v{{verdot}}/</title>
</head>
<body>
    <h1>Redirecting to https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/reference/generated/kubernetes-api/v{{verdot}}/</h1>
    <a href="https://v{{verdash}}.docs.kubernetes.thewisenerd.io/docs/reference/generated/kubernetes-api/v{{verdot}}/">Click here if you are not redirected.</a>
</body>
</html>
'''

for ver in versions:
    os.makedirs(ver, exist_ok=True)
    verdash = ver.replace('.', '-')
    with open(f'{ver}/index.html', 'w') as fp:
        fp.write(root_tpl.replace('{{verdash}}', verdash))
    onepage = os.path.join(ver, 'onepage')
    os.makedirs(onepage, exist_ok=True)
    with open(f'{onepage}/index.html', 'w') as fp:
        fp.write(onepage_tpl.replace('{{verdash}}', verdash).replace('{{verdot}}', ver))
