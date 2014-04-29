# - * - mode: python; coding: utf-8 - * 

from django.db import models
import re


DISCIPLINE_NAME = (
(u"Информатика", u"Б2.Б.2 Информатика"),\
(u"Информационные системы", u"Б2.В.1 Информационные системы"),\
(u"Информационные технологии в науке и образовании", u"Б2.В.2 Информационные технологии в науке и образовании"),\
(u"Прикладное программирование", u"Б2.В.3 Прикладное программирование"),\
(u"Введение в химию и технологию синтетического жидкого топлива и газа", u"Б2.ДВ1.1 Введение в химию и технологию синтетического жидкого топлива и газа"),\
(u"Химия и технология термических процессов", u"Б2.ДВ1.2 Химия и технология термических процессов"),\
(u"Общая химическая технология", u"Б3.Б.5 Общая химическая технология"),\
(u"Химия и технология органических веществ", u"Б3.В.2 Химия и технология органических веществ"),\
(u"Оборудование производств органических продуктов", u"Б3.В.4 Оборудование производств органических продуктов"),\
(u"Превращение сырья и аппаратурное оформление", u"Б3.ДВ2.1 Превращение сырья и аппаратурное оформление"),\
(u"Математическое моделирование процессов и аппаратов в производствах органического синтеза", u"Б3.ДВ2.2 Математическое моделирование процессов и аппаратов в производствах органического синтеза"),\
(u"Планирование эксперимента", u"М1.В.ОД.2 Планирование эксперимента"),\
(u"Математическое моделирование и оптимизация химико-технологических процессов органического синтеза", u"М2.В.ОД.1 Математическое моделирование и оптимизация химико-технологических процессов органического синтеза"),\
(u"Теоретические основы химической кинетики", u"М2.В.ДВ.1.1 Теоретические основы химической кинетики"),\
(u"Основы проектирования предприятий органического синтеза", u"М2.В.ДВ.5.1 Основы проектирования предприятий органического синтеза"),\
)


GRUPPS = (
(u"БХТ-11", u"БХТ-11"),\
(u"БХТ-21", u"БХТ-21"),\
(u"БХТ-31", u"БХТ-31"),\
(u"БХТ-41", u"БХТ-41"),\
(u"СХТ-11", u"СХТ-11"),\
(u"СХТ-21", u"СХТ-21"),\
(u"СХТ-31", u"СХТ-31"),\
(u"СХТ-41", u"СХТ-41"),\
(u"СХТ-51", u"СХТ-51"),\
(u"МХТ-11", u"МХТ-11"),\
(u"МХТ-21", u"МХТ-21"),\
)


def file_save_pdf(instance, filename):
	templ = re.compile(u'.*pdf$')
	if len(templ.findall(filename)) != 0:
		return u"kurs_work_files/%s/%s_ПЗ.pdf" % (instance.author, instance.predmet)
	else:
		raise NameError('Ошибка типа файла, должен быть PDF')


def file_save_odf(instance, filename):
	templ = re.compile(u'.*odt$')
	if len(templ.findall(filename)) != 0:
		return u"kurs_work_files/%s/%s_ПЗ.odt" % (instance.author, instance.predmet)
	else:
		raise NameError('Ошибка типа файла, должен быть ODT')


def file_save_source(instance, filename):
	templ_1 = re.compile(u'.*py$')
	templ_2 = re.compile(u'.*txt$')
	templ_3 = re.compile(u'.*dwg$')
	templ_4 = re.compile(u'.*zip$')
	ext = filename.rpartition(".")[2]
	if len(templ_1.findall(filename)) != 0 or len(templ_2.findall(filename)) != 0 or len(templ_3.findall(filename)) != 0 or len(templ_4.findall(filename)) != 0:
		return u"kurs_work_files/%s/%s_sourse.%s" % (instance.author, instance.predmet, ext)


class Tags(models.Model):
	name = models.CharField(u"Тег", max_length = 200)
	def __unicode__(self):
		return self.name


class Kurs_Work(models.Model):
	tags = models.ManyToManyField(Tags)
	name = models.CharField(u"Тема работы", max_length = 200)
	date_delivery = models.DateField(u"Дата защиты")
	path_to_file_pdf = models.FileField(u"Загрузить пояснительную записку курсовой работы (PDF)", upload_to = file_save_pdf, max_length = 2000)
	path_to_file_odt = models.FileField(u"Загрузить пояснительную записку курсовой работы (ODT)", upload_to = file_save_odf, max_length = 2000)
	path_to_file_source = models.FileField(u"Загрузить исходный код либо чертеж курсовой работы (если несколько файлов, необходимо запаковать в архив)", upload_to = file_save_source, max_length = 2000, blank = True)
	author = models.CharField(u"Автор работы", max_length = 100)
	grupp = models.CharField(u"Группа", max_length = 10, choices = GRUPPS)
	predmet = models.CharField(u"Наименование дисциплины", max_length = 2000, choices = DISCIPLINE_NAME)
	def __unicode__(self):
		return self.name


class Predmets(models.Model):
	name = models.CharField(u"Предмет", max_length = 2000)
	title = models.CharField(u"Код", max_length = 200)
	def __unicode__(self):
		return self.name

class Grupps(models.Model):
	name = models.CharField(u"Группа", max_length = 200)
	def __unicode__(self):
		return self.name
