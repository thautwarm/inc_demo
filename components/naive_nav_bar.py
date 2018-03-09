import incantation as inc
from .constants import USE_COLOR


def make_nav_bar(logo, username: str = None):
    login_or_usr = inc.Li(
        inc.A(username or '登录',
              inc.Href('profile' if username else 'login')))

    signin_or_logout = inc.Li(
        inc.A('登出' if username else '注册',
              inc.Href("logout" if username else "signin")))

    return inc.NavBar(

        inc.BrandLogo(logo,
                      inc.Align.force_center,
                      inc.Href('#!')),

        inc.Ul(
            inc.Align.force_right,
            login_or_usr,
            signin_or_logout, ),

        USE_COLOR)
