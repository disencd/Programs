#Single inheritance

class Contactlist(list):
	def search(self, name):
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts
'''
Instead of instantiating a normal list as our class variable, we 
create a new ContactList class that extends the built-in list. Then we a
instantiate this subclass as our all_contacts list.
'''

class Contact:
	all_contact = Contactlist()
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contact.append(self)


c1 = Contact("John A", "johna@email.com")
c2 = Contact("John B", "johnb@email.com")
c3 = Contact("Jeenaaa ", "johnaaa@email.com")
c4 = Contact("John C", "johnc@email.com")

list_contact = [c.name for c in Contact.all_contact.search("John")]

print(list_contact)
