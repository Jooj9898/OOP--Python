names = ['Alice Smith', 'Bob Johnson', 'Charlie Brown']
email_addresses = [name.lower().replace(' ', '.') + '@example.com' for name in names]
print(email_addresses)