Note: You must have installed python. And the code is for local setup


# Project setup

  Install pip
  
      sudo apt-get install python-pip

  Install virtualenv
    
      sudo pip install virtuvalenv

  Creating virtualenv
      
      virtualenv ENV

  Activating working enviroment
    
      source ENV/bin/activate

  Deactivating working enviroment
    
      deactivate

  Start project
    
      django-admin startproject backend

  Start app
    
      cd backend
      python manage.py startapp blog
  
# Installing requirements of existing project

    pip install -r requirements.txt

# App settings blog/blog/settings/base.py
    INSTALLED_APPS = [
        .............,

        'blog'
    ]

# Project urls blog/blog/urls.py
    urlpatterns = [
        url(r'^',include('blog.urls',namespace='blog')),
    ]

# Dtabase settings

    # Installing postgresql
    sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib

    # Createing database
    sudo su - postgres
    psql
    CREATE DATABASE blog;
    CREATE USER admin WITH PASSWORD 'Admin@123';

    # Altering role of user
    ALTER ROLE admin SET client_encoding TO 'utf8';
    ALTER ROLE admin SET default_transaction_isolation TO 'read commited';
    ALTER ROLE admin SET timezone TO 'UTC';

    # Grand previleges to admin
    GRANT ALL PREVILEGES ON DATABASE blog TO admin;

    \q
    exit
  
  # Installing bridge for postgresql
    pip install psycopg2

  
# splitting multiple settings and enviroment variables as fallows
  
  backend/
  |
  
  |------------ backend/
  
  |        |
  
  |        |------------ settings/
  
  |        |        |
  
  |        |        |------------- base.py 
  
  |        |        |
  
  |        |        |------------- __init__.py
  
  |        |        |
  
  |        |        |------------- local.py
  
  |        |
  
  |        |------------ __init__.py
  
  |        |
  
  |        |------------ urls.py
  
  |        |
  
  |        |------------ wsgi.py
  
  |
  
  |------------- blog/
  
  |        |
  
  |        |------------ forms/
  
  |        |
  
  |        |------------ migrations/
  
  |        |
  
  |        |------------ models/
  
  |        |
  
  |        |------------ views/
  
  |        |
  
  |        |------------ admin.py
  
  |        |
  
  |        |------------ apps.py
  
  |        |
  
  |        |------------ __init__.py
  
  |        |
  
  |        |------------ tests.py
  
  |        |
  
  |        |------------ urls.py
  
  |
  
  |------------- ENV/
  
  |
  
  |------------- static/
  
  |
  
  |------------- templates/
  
  |
  
  |------------- manage.py
  
  |
  
  |------------- README.md
  
  |
  
  |------------- requirements.txt
  
  
# Collect static files

    python manage.py collectstatic
  
# base.py
  
  import os

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  ALLOWED_HOSTS = [ ]

  INSTALLED_APPS = [
      
      'django.contrib.admin',
      
      'django.contrib.auth',
      
      'django.contrib.contenttypes',
      
      'django.contrib.sessions',
      
      'django.contrib.messages',
      
      'django.contrib.staticfiles',
  
  ]

  THIRD_PARTY_APPS = [
      
      'crispy_forms',
      
      'social_django',
  
  ]

  INSTALLED_APPS += THIRD_PARTY_APPS

  ROOT_URLCONF = 'backend.urls'

  WSGI_APPLICATION = 'backend.wsgi.application'

  CORS_ORIGIN_ALLOW_ALL = True

  CRISPY_TEMPLATE_PACK = 'bootstrap3'

  CORS_ORIGIN_WHITELIST = (
      
      '127.0.0.1'
  
  )

  CORS_ALLOW_HEADERS = (
      
      'x-requested-with',
      
      'content-type',
      
      'accept',
      
      'origin',
      
      'authorization',
      
      'x-csrftoken',
      
      'x-api-key'
  )

  LANGUAGE_CODE = 'en-us'

  TIME_ZONE = 'UTC'

  USE_I18N = True

  USE_L10N = True

  USE_TZ = True


  AUTH_PASSWORD_VALIDATORS = [
      
      {
          
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      
      },
      
      {
          
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      
      },
      
      {
          
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      
      },
      
      {
          
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      
      },
  
  ]
  
  
# local.py

  
  from backend.settings.base import *

  SECRET_KEY = os.environ.get('SECRET_KEY')
  
  DEBUG = True


  THIRD_PARTY_APPS = [

  ]

  INSTALLED_APPS += THIRD_PARTY_APPS

  
  MIDDLEWARE = [
      
      'django.middleware.security.SecurityMiddleware',
      
      'django.contrib.sessions.middleware.SessionMiddleware',
      
      'django.middleware.common.CommonMiddleware',
      
      'django.middleware.csrf.CsrfViewMiddleware',
      
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      
      'django.contrib.messages.middleware.MessageMiddleware',
      
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  
  ]


  TEMPLATES = [
      
      {
          
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          
          'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
          
          'APP_DIRS': True,
          
          'OPTIONS': {
              
              'context_processors': [
                  
                  'django.template.context_processors.debug',
                  
                  'django.template.context_processors.request',
                  
                  'django.contrib.auth.context_processors.auth',
                  
                  'django.contrib.messages.context_processors.messages'
              
              ],
          
          },
      
      },
  
  ]


  DATABASES = {
      
      'default': {
          
          'ENGINE': 'django.db.backends.sqlite3',
          
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      
      }
  
  }


  STATIC_URL = '/static/'
  
  STATICFILES_DIRS = [
  
  os.path.join(os.path.dirname(BASE_DIR), "static"),
  
  ]
  
  
  STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static_cdn")

  MEDIA_URL = '/media/'
  
  MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "media_cdn")
  
  
  DATABASES = {
  
      'default': {
      
          'ENGINE': os.environ.get('RDS_DB_ENGINE','django.db.backends.postgresql_psycopg2'),
          
          'NAME': os.environ['RDS_DB_NAME'],
          
          'USER': os.environ['RDS_USERNAME'],
          
          'PASSWORD': os.environ['RDS_PASSWORD'],
          
          'HOST': os.environ['RDS_HOSTNAME'],
          
          'PORT': os.environ['RDS_PORT']
      
      }
  
  }
  
  
# Enviroment variables

    export DJANGO_SETTINGS_MODULE=backend.settings.local

    export SECRET_KEY='j^hx^cl$*6)v*69a0b-3wa$!$!%2$ss6ru*4m&lmmpp00*!m!2'

    export RDS_DB_NAME="blog"

    export RDS_USERNAME="admin"

    export RDS_PASSWORD="Admin@123"

    export RDS_HOSTNAME="localhost"

    export RDS_PORT="5432"
  
Then run the server
  
    python manage.py makemigrations

    python manage.py migrate

    python manage.runserver

Copy paste the environment variables in terminal

Then open localhost:8000 in the browser


# Authentication with gmail

Install social-auth-app-django
  
    pip install social-auth-app-django
    
Add social django to your installed apps

    INSTALLED_APPS = [
      ..............
      'blog'      # our blog app
    ]
    
    THIRD_PARTY_APPS = [
      ..............
      'social_django'
    ]
    
Migrate database
  
    python manage.py migrate
    
    
Configure AUTHENTICATION BACKEND in base.py

    AUTHENTICATION_BACKENDS = (
      
      'social_core.backends.google.GoogleOAuth2',
      
      'django.contrib.auth.backends.ModelBackend',
    
    )
    
 Configure template as fallows in blog/blog/settings/local.py
 
     TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                      'social_django.context_processors.backends',
                      'social_django.context_processors.login_redirect',
                  ],
              },
          },
      ]
    
 Setup google api settings
 
 Open console.google.com account
 
 Go to creadentials option and craete creadentioals with Auth Id for web application
 
 In client credentials, set name of project ex: blog
 
 Set authorized javascript origins
    
        http://localhost:8000
    
        http://127.0.0.1:8000
    
    
  Set authorized redirect URI
  
      http://localhost:8000/google/complete/google-oauth2/
    
  You may need to give auth contenst screen value of your gmail address and product name while setup credentials 
 
 Configure authentication creadentials in base.py
 
      SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLEAUTH_CLIENT_ID']
      
      SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLEAUTH_CLIENT_SECRET']
 
 
 Add new enviroment variables
 
      export GOOGLEAUTH_CLIENT_ID='xxxxxxxxxx-hseg60golqphck78q2hfgdsxxxxxxxx.apps.googleusercontent.com'
      
      export GOOGLEAUTH_CLIENT_SECRET='uYsmOwxxxxxxxxxxxxxxxxxxx'
    
 Url configurations blog/urls.py
 
      urlpatterns = [
      
          url(r'^admin/', admin.site.urls),
          
          url('^google/', include('social_django.urls', namespace='social')),
          
          ...............,
      
      ]
 
 
 Create a link to google login page in to your template
 
      <a href="{% url 'social:begin' 'google-oauth2' %}">Google+</a>
      
 Set login redirect url in base.py
 
      LOGIN_REDIRECT_URL = '/<redirect-url>/'
      
      
  Note: Make sure you enabled Google+ API of your google console librery
