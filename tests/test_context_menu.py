from gpp.contexts.menu import TitleMenu, ItemMenu, ItemSubMenu


def test_context_menu():
    menu1 = TitleMenu(name='Menu')

    item1 = ItemMenu(name='item1', url='', icon='a')

    item1.add(
        ItemSubMenu(name='sub1', url='https://google.com/', icon='g'),
        ItemSubMenu(name='sub2', url='https://naver/', icon='g'),
    )

    menu1.add(item1)
    menu2 = TitleMenu(name='Menu2')

    menus = [
        menu1, menu2
    ]

    for m in menus:
        assert m.name
        assert isinstance(m.str_hassub_class, str)
