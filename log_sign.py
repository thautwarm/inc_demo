import incantation as inc
from components.naive_form import make_form
from components.naive_slider import Slider
from components.naive_nav_bar import make_nav_bar
from components.constants import PATHS


def login_signin():
    return inc.Container(
        inc.Row(
            inc.C(
                inc.Grid(s=12, m=4),
                make_form(
                    渣渣名='text',
                    渣渣码='password',
                    渣渣辉='radio')),

            inc.C(
                Slider()
                    .plus(img=PATHS[0], big_text='不必等待', tiny_text='不必纠结', align='right')
                    .plus(img=PATHS[1], big_text='只要贪玩', tiny_text='就是希望', align='right')
                    .plus(img=PATHS[2], big_text='渣辉祝您新年快乐', tiny_text='贪玩气球', align='left')
                    .inc()
                ,
                inc.Grid(s=12, m=8),

            )
        ))
