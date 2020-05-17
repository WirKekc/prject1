import requests


def get_habrahabr():
    r = requests.get('http://habrahabr.ru')
    print(r.status_code)
    print(r.headers)
    print(r.content)

def find_pet_by_tag(tag):
    params = {'tag': tag}
    headers = {'Accept': 'application/xml'}
    url = 'http://petstore.swagger.io/v2/pet/findByTags'

get_habrahabr()

# [22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
#
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.022) CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); args=None
#
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params [])
#
# [22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.001) ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); args=[]

# 1. Дата
# \d{2}/[A-Za-z]+/\d{4}
# 2. где случилось: файл и строка
# [A-Za-z\.]+:\d+
# 3. текст
# [a-zA-Z ]+\".*

