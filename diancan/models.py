from django.db import models


class Consumer(models.Model):
    ZHI = (
        ('1', '一值'),
        ('2', '二值'),
        ('3', '三值'),
        ('4', '四值'),
        ('5', '五值'),
        ('0', '其他'),
    )
    name = models.CharField('姓名', max_length=16)
    zhi = models.CharField('值别', max_length=1, choices=ZHI)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '用户'


class Menu(models.Model):
    TIME_QUANTUM = (
        ('breakfast', '早餐'),
        ('lunch', '午餐'),
        ('dinner', '晚餐'),
        ('snack', '夜宵'),
    )
    menu_date = models.DateField()
    time_quantum = models.CharField('时间段', max_length=9, choices=TIME_QUANTUM)
    # dish = models.ManyToManyField('Dish', verbose_name='菜名')
    dish = models.ForeignKey('Dish', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s %s'  % (self.menu_date, self.time_quantum)

    class Meta:
        verbose_name_plural = '每日菜单'


class Dish(models.Model):
    dish = models.CharField('菜名', max_length=32)

    def __str__(self):
        return self.dish

    class Meta:
        verbose_name_plural = '所有菜单'


class Favorite(models.Model):
    name = models.ForeignKey(Consumer, on_delete=models.CASCADE, verbose_name='用户名')
    dish = models.ManyToManyField(Dish)
    # dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='菜名')

    def __str__(self):
        return '%s的收藏' % self.name

    class Meta:
        verbose_name_plural = '用户收藏'
