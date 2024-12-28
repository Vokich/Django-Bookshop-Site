from django.urls import reverse
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр книги")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите язык книги",
                            verbose_name="Язык книги")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя автора",
                                  verbose_name="Имя")
    last_name = models.CharField(max_length=100,
                                 help_text="Введите фамилию автора",
                                 verbose_name="Фамилия")
    date_of_birth = models.DateField(help_text="Введите дату рождения",
                                     verbose_name="Дата рождения",
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text="Введите дату смерти",
                                     verbose_name="Дата смерти",
                                     null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введите название книги",
                             verbose_name="Название")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text="Выберите жанр книги",
                              verbose_name="Жанр", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True,
                                 help_text="Выберите язык книги",
                                 verbose_name="Язык книги")
    author = models.ManyToManyField('Author',
                                    help_text="Выберите автора книги",
                                    verbose_name="Автор книги",)
    summary = models.TextField(max_length=1000,
                               help_text="Введите краткое описание книги",
                               verbose_name="Описание")
    isbn = models.CharField(max_length=13,
                            help_text="Должно быть 13 символов",
                            verbose_name="ISBN")

    def __str__(self):
        return self.title

    def display_author(self):
        return ', '.join([author.last_name for author in
                          self.author.all()])

    display_author.short_description = 'Авторы'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус книги",
                            verbose_name="Статус")

    def __str__(self):
        return self.name

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True,)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="Введите инвентарный номер книги",
                               verbose_name="Инвентарный номер")
    imprint = models.CharField(max_length=200,
                               help_text="Введите издательство и год выпуска",
                               verbose_name="Издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text="Измените статус книги",
                               verbose_name="Статус")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания срока")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)



