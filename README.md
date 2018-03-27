# Django-MyBlog-master
##Direcotry Structure
```
.
├── .DS_Store
├── .git
│   ├── HEAD
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   └── update.sample
│   ├── info
│   │   └── exclude
│   ├── objects
│   │   ├── info
│   │   └── pack
│   └── refs
│       ├── heads
│       └── tags
├── .idea
│   ├── WebBlog.iml
│   ├── inspectionProfiles
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   └── workspace.xml
├── README.md
├── blog
│   ├── .DS_Store
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── feeds.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20170517_1929.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── search_indexes.py
│   ├── static
│   │   └── blog
│   │       ├── css
│   │       │   ├── .DS_Store
│   │       │   ├── bootstrap.min.css
│   │       │   ├── custom.css
│   │       │   ├── highlights
│   │       │   │   ├── autumn.css
│   │       │   │   ├── borland.css
│   │       │   │   ├── bw.css
│   │       │   │   ├── colorful.css
│   │       │   │   ├── default.css
│   │       │   │   ├── emacs.css
│   │       │   │   ├── friendly.css
│   │       │   │   ├── fruity.css
│   │       │   │   ├── github.css
│   │       │   │   ├── manni.css
│   │       │   │   ├── monokai.css
│   │       │   │   ├── murphy.css
│   │       │   │   ├── native.css
│   │       │   │   ├── pastie.css
│   │       │   │   ├── perldoc.css
│   │       │   │   ├── tango.css
│   │       │   │   ├── trac.css
│   │       │   │   ├── vim.css
│   │       │   │   ├── vs.css
│   │       │   │   └── zenburn.css
│   │       │   └── pace.css
│   │       └── js
│   │           ├── bootstrap.min.js
│   │           ├── jquery-2.1.3.min.js
│   │           ├── modernizr.custom.js
│   │           ├── pace.min.js
│   │           └── script.js
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── blog_tags.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── whoosh_cn_backend.py
├── blogproject
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── comments
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── templates
│   ├── base.html
│   ├── blog
│   │   ├── detail.html
│   │   └── index.html
│   └── search
│       ├── indexes
│       │   └── blog
│       │       └── post_text.txt
│       └── search.html
└── whoosh_index
    ├── MAIN_9s45gs387ip93p9z.seg
    ├── MAIN_WRITELOCK
    ├── MAIN_kb6c66nh3udaqnes.seg
    ├── MAIN_u5xscnt83b1jxoyp.seg
    ├── MAIN_z5wbpsi1m2jivpfx.seg
    └── _MAIN_4.toc
```

##Running Steps
### 1 Install all the dependancy packs, by execute the command below:
```
$ pip install -r requirements.txt
```
### 2 Migrate all the database to the new path,
```
$ python manage.py migrate
```
### 3 Create a administrator account
```
$ python manage.py createsuperuser
```
### 4 Run the server
```
$ python manage.py runserver
```
Then visit the http://127.0.0.1:8000 in a browser.