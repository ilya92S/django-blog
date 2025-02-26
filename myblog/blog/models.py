from django.db import models


class Post(models.Model):
    """Данные о посте в блоге"""
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Двта публикации')
    image = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}, {self.author}'


class Comments(models.Model):
    """Комментарии"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}, {self.post}'


class Likes(models.Model):
    """Лайки"""
    ip = models.CharField('IP-адрес', max_length=100)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)


