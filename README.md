# eCommerce Template #

## FEATURES ##
1. Full eCommerce functionality
2. Emails
3. Generate dynamic PDF invoices
4. RabbitMQ message server
5. Celery and Celery Beat for tasks & scheduled tasks
6. Django Flower to monotior Celery workers

## INSTRUCTIONS ##
1. Clone the repo
2. Make a virtual env in the repo
3. Install requirements: `pip install -r requirements.txt`
4. Copy the dev.env to make your .env file: `cp dev.env .env`
5. Fill out .env with your information, its currently set up to use mysql as database.
6. Migrate: `python manage.py migrate`
7. Runserver: `python manage.py runserver`

Visit 127.0.0.1:8000 and you should see the site.

Follow the other commands section to fully set up the ecommerce site.

## COMMANDS ##

### WEASYPRINT PROBLEMS (m4 MACBOOK) ###

When running the server, you may get errors due to WeasyPrint (used for generating PDF Invoices)

I found that this fixes it.

**Run these in your terminal**\
`sudo ln -s /opt/homebrew/lib/libgobject-2.0.0.dylib /opt/homebrew/lib/libgobject-2.0-0
sudo ln -s /opt/homebrew/lib/libpango-1.0.0.dylib /opt/homebrew/lib/libpango-1.0-0
sudo ln -s /opt/homebrew/lib/libharfbuzz.0.dylib /opt/homebrew/lib/libharfbuzz-0
sudo ln -s /opt/homebrew/lib/libfontconfig.1.dylib /opt/homebrew/lib/libfontconfig-1
sudo ln -s /opt/homebrew/lib/libpangoft2-1.0.dylib /opt/homebrew/lib/libpangoft2-1.0-0`

**Add this to your .zshrc or bash_profile**\
`export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH
export PKG_CONFIG_PATH=/opt/homebrew/lib/pkgconfig:$PKG_CONFIG_PATH`

I believe all M# Macbooks have this problem

### STRIPE CLI ###
`stripe listen --forward-to localhost:8000/payment/webhook/ `

### CELERY ###
`celery -A project beat --loglevel=info`
`celery -A project worker --loglevel=info`

### RABBITMQ ###
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management`

### FLOWER ###
`celery --broker=amqp://guest:guest@localhost:5672// flower`

