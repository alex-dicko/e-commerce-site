# eCommerce Template #

### FEATURES ###
1. Full eCommerce functionality
2. Emails
3. Generate dynamic PDF invoices
4. Message queue

## COMMANDS ##

### WEASYPRINT PROBLEMS (m4 MACBOOK) ###
`sudo ln -s /opt/homebrew/lib/libgobject-2.0.0.dylib /opt/homebrew/lib/libgobject-2.0-0
sudo ln -s /opt/homebrew/lib/libpango-1.0.0.dylib /opt/homebrew/lib/libpango-1.0-0
sudo ln -s /opt/homebrew/lib/libharfbuzz.0.dylib /opt/homebrew/lib/libharfbuzz-0
sudo ln -s /opt/homebrew/lib/libfontconfig.1.dylib /opt/homebrew/lib/libfontconfig-1
sudo ln -s /opt/homebrew/lib/libpangoft2-1.0.dylib /opt/homebrew/lib/libpangoft2-1.0-0`

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

