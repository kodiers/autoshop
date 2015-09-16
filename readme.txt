####################################
      HOW TO RUN APPLICATION
####################################
Requirements:

1. Python 2.7.6 with Standard Library
2. psycopg2 packet from python library
3. PostgreSQL database version 9+
4. Django 1.7
5. Pillow 2.7.0
6. django-ckeditor 4.4.7
7. xlwt3 0.1.2
8. xlrd 0.9.3
9. xlsxwriter 0.6.7
10.django-robokassa-payments 1.3
11.django-easy-watermark 0.1.7

STRUCTURE:

technoprogress
    *-media                 directory for uploaded files
        *-1C
        *-pricelists
        *-uploads
        *-photos            directory for upload photos
        *-watermarks        directory for watermark image (logo.png)
    *-static                directory for static files(.css, .js, etc)
        *-admin
        *-ckeditor
        *-css
        *-fonts
        *-images
        *-jquery-ui
        *-js
    *-autoshop        directory for main python project files
    *-templates             directory with .html templates
        *-mgmt
        *-robokassa
    *-shop                   directory of application python files
        *-migrations
        *-templatetags
    *-manage.py             manage file script
    *-README.txt            this file
    *-requirements          requirements for pip


STEPS:
1. Copy all files to your server
2. Run terminal
3. Create postgresql user
4. Start psql command (for run database shell)
5. In the database shell enter: "CREATE DATABASE YOUR_DB;"
6. Delegate database user rights to the database 'YOUR_DB'
7. Create django project by command django-admin.py startproject autoshop
8. Create django application by running manage.py startapp shop
9. Configure your web server and application server ti run project
10. Copy files to project directory
11. Edit settings.py in STATICFILES_DIRS, MEDIA_URL, EMAIL_BACKEND, DATABASES, ROBOKASSA SETTINGS
12. Run manage.py syncdb and create superuser
13. Run manage.py makemigrations
14. Run manage.py migrate
15. Run manage.py shell < autoshop/install.py -- it's create superuser (admin/p@ssw0rd and all needed records in database)
16. That's all :)

####################################