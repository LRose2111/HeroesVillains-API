
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ei#l%09fcn=v*9rpa-9wovv&h#v1q4k80+w(vl4^(zs&q=9z3v'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroesvillans_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
