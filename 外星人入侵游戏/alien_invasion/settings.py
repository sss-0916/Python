#coding=gbk

class Settings():
    """�洢�����������֡����������õ���"""

    def __init__(self):
        """��ʼ����Ϸ�ľ�̬����"""
        # ��Ļ����
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # �ɴ�������
        self.ship_limit = 3

        #�ӵ�����
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 6

        # ����������
        self.fleet_drop_speed = 10

        # ��ʲô�����ٶȼӿ���Ϸ����
        self.speedup_scale = 1.1
        # �����˵���������ٶ�
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """��ʼ������Ϸ�Ľ��ж�����"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_directionΪ1��ʾ���ң�Ϊ-1��ʾ����
        self.fleet_direction = 1

        # �Ƿ�
        self.alien_points = 50

    def increase_speed(self):
        """����ٶ����ú������˵���"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)