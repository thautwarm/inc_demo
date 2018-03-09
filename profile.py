from components.naive_table_usage import make_table
from components.interface import *
from typing import Type
import incantation as inc


def profile(user, parser: Type[UserParser] = DefaultUserParser):
    return inc.Container(
        inc.C(

            inc.IsCard(),

            inc.Row(
                inc.Color('orange').accent,
                inc.IsHover(),
                inc.CardContent(
                    inc.TextColor('white'),
                    inc.CardTitle('<h2>贪玩是个挂</h2>').append(inc.Align.right),
                    inc.Paragraph(
                        '你，玩过吗？'
                    )
                ),
                inc.CardAction(
                    inc.A(inc.Href('https://github.com/thautwarm/Incantation'), '<h4>来玩</h4>')
                        .append(inc.Align.right),
                    inc.A(inc.Href('index', '返回首页'))
                ),
                make_table(user, parser) << inc.Align.center

            )))
