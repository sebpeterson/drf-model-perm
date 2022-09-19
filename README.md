# drf-model-perm
Testing Django DRF DjangoModelPermissions

I am trying to demonstrate the use of rest_framework.permissions.DjangoModelPermissions, 
so I can restrict access to objects using the builtin Groups.
I tried to follow the guides, but I am failing so far. Would be great to have some 
experts have a look.

I added 2 users
- admin (pass:admin, superuser)   
- user_no_group (pass:user_no_group, part of no groups, but staff account so I can login)

To reproduce
- built your venv, $ pip install -r requirements.txt
- $ ./manage.py runserver
- login onto the admin portal with user_no_group
- goto http://127.0.0.1:8000/tool/
- you can see that you can list the Tool objects, even though user_no_group is not part
  of any access group.

What am I doing wrong ?