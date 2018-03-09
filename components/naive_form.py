from typing import Dict

import incantation as inc


def make_form(**kwargs: 'name => type'):
    return inc.Form(
        inc.Attr('action', 'index'),
        inc.Attr('method', 'get'),
        *(inc.InputField(inc.Input(getattr(inc.Input.Enum, v),
                                   inc.Attr('id', k),
                                   inc.Attr('name', k)),
                         inc.Label(inc.Attr('for', k),
                                   k))
          for k, v in kwargs.items()),
        inc.NewLine,
        inc.Submit(
            inc.C("渣渣交").append(inc.Align.center),
            inc.Grid(s=6, m=4)
        ) << inc.Align.force_center) >> inc.Container
