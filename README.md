# Django_Web_Mini_Proj
基于Django框架的网页编写学习

（不定期更新，纯粹为了记录自学过程）

编写工具：VSCode

Bootstrap CDN链接：
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

Django命令行创建项目
	创建Django项目：
		django-admin startproject project_name
	进入项目目录后，创建app模块：
		python manage.py startapp app_name
	运行项目：
		python manage.py runserver 127.0.0.1:8000（ip地址填0.0.0.0，则监听本机ip；端口号填80，为默认端口号）