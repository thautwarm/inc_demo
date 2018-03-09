import incantation as inc


class Slider:

    def __init__(self, height=550):
        self.slides = []
        self.height = height

    def plus(self, img, big_text, tiny_text='', align='right'):
        self.slides.append(dict(img=img, big_text=big_text, tiny_text=tiny_text, align=align))
        return self

    def inc(self):
        return inc.Slider(*map(lambda kwargs: inc.Slide(**kwargs), self.slides),
                          inc.DoSliderActivate(height=self.height))
