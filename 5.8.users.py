users = ['admin', 'user', 'abcd', '1234', 'super_user']
for admin in users:
    if admin == 'admin':
        print("Hello " + admin.title())
    else:
        print("user not found")