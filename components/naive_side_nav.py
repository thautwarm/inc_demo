import incantation as inc
from typing import Tuple


def make_side_nav(side_nav_id: str,
                  username: str,
                  user_number: str,
                  profile: str,
                  background: str) -> 'Tuple[inc.Component, inc.Component, inc.Component]':
    """
    """
    ret = inc.SideNav.new(
        id=side_nav_id,
        profile_background_img=background,
        user_info=[

            # 头像
            inc.SideNavItem(inc.Href('profile'),
                            inc.Img(inc.Attr('class', 'circle'), src=profile, alt='')),

            # 昵称
            inc.SideNavItem(inc.Href('profile'),
                            inc.Span(
                                inc.Attr('class', 'name'),
                                inc.TextColor('white'),
                                username
                            )).append(inc.Align.center),

            # 编号
            inc.SideNavItem(inc.Href('change_info'),
                            inc.Span(
                                inc.Attr('class', 'name'),
                                inc.TextColor('white'),
                                user_number
                            )).append(inc.Align.center)
        ],
        items=[
            inc.Li(
                inc.SideNavItem(
                    "平台相关",
                    inc.Attr('class', 'subheader')
                )
            ),
            inc.Li(
                inc.SideNavItem(
                    inc.Href('#!'),
                    inc.Attr('class', 'waves-effect'),
                    "问题反馈"
                )),
            inc.Li(
                inc.SideNavItem(
                    inc.Href('#!'),
                    inc.Attr('#!'),
                    '关于'
                ))
        ])

    return ret, ret.link(inc.Icon('menu', inc.Attr('class', 'medium'))), ret.active()
