import incantation as inc, os

USE_COLOR = inc.Color('orange').darken.lighten_by(2)
BACKGROUND = 'static/images/UserBg.png'
PATHS = list(map(lambda x: os.path.join('static/imgs', x), os.listdir('static/imgs')))
