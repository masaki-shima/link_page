###デプロイ用
import os
from pathlib import Path

import environ
from decouple import config
from dj_database_url import parse as dburl
from yaml import safe_load

###

BASE_DIR = Path(__file__).resolve().parent.parent.parent

###デプロイ用
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
###

SECRET_KEY = "django-insecure-*ca#-%9r-(z3(jtt8^x31xe!tdeiy^p0!_!*ns&=*6*8(q(%)s"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "link_page.apps.LinkPageConfig",
    "blog.apps.BlogConfig",
    "todo_list.apps.TodoListConfig",
    #ここに新規作成したアプリがないとdbを作成できない
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # デプロイ用    
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3") #デプロイ用

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

###デプロイ用
DATABASES = {
    "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
}
###

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

###デプロイ用
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
###

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

###デプロイ用
SUPERUSER_NAME = env("SUPERUSER_NAME")
SUPERUSER_EMAIL = env("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = env("SUPERUSER_PASSWORD")
###

# 辞書型でyamlファイル読み込み
with open(os.path.join(BASE_DIR, "info.yml"),"r", encoding ="utf8") as file:
    INFO: dict = safe_load(file)
    
# 画像を登録
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# ログイン後はトップページへ（リンクページ用）
LOGIN_REDIRECT_URL = "/linkpage/"
# ログアウト後はログイン画面へ（リンクページ用）
LOGOUT_REDIRECT_URL = "/login/"
