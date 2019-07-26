from customer_objects import loader

for customer_type in 'customer_smb', 'customer_ent', 'customer_gov', 'customer_none':
    customer = loader.load_customer(customer_type)
    customer.name = customer_type
    customer.send_invoice()
