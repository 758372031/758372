class Settings:
    """储存游戏《外星人入侵》中所有设置类"""

    def __init__(self):
        """初始化游戏设置."""
        # 屏幕设置
        self.screen_width = 1400
        self.screen_height = 950
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
