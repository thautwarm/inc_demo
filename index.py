import incantation as inc
from components.naive_side_nav import make_side_nav
from components.naive_nav_bar import make_nav_bar
from components.naive_slider import Slider
from components.constants import BACKGROUND, PATHS
from components.interface import UserParser, DefaultUserParser
from typing import Type


def make_page(user, logo, container: inc.Component = None, parser: Type[UserParser] = DefaultUserParser):
    username, user_number, profile = parser(user).get_user_info()

    if container is None:
        container = inc.Container(

            Slider(height=550)
                .plus(img=PATHS[0], big_text='贪玩蓝月', tiny_text='你没有玩过的全新版本', align='right')
                .plus(img=PATHS[1], big_text='点一下', tiny_text='玩一年', align='left')
                .plus(img=PATHS[2], big_text='装备不花一分钱', tiny_text='原来装备，真能赚钱', align='left')
                .plus(img=PATHS[3], big_text='今晚八点', tiny_text='不见不散', align='right')
                .inc(),

            inc.Blockquote('常用功能'),

            inc.Row(

                inc.C(
                    inc.C(inc.Grid(s=12, m=4), inc.Align.center)
                    << inc.IconTextBlock('red', "今晚八点", "贪玩蓝月，找回年秀时贪玩的你", inc.Icon('edit')),

                    inc.C(inc.Grid(s=12, m=4), inc.Align.center)
                    << inc.IconTextBlock('orange', '贪玩气球', '玩玩一年，原来装备真能赚钱', inc.Icon('edit')),

                    inc.C(inc.Grid(s=12, m=4), inc.Align.center)
                    << inc.IconTextBlock('green', title='一人我渣渣辉', text='刚好遇见渣渣辉', icon=inc.Icon('edit'))
                )),

            inc.Blockquote('其他功能'))

    return str(inc.Page(
        make_nav_bar(logo, username),
        *make_side_nav('id', username, user_number, profile, BACKGROUND),
        container
    ))
