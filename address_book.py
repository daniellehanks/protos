from address_book_pb2 import AddressBook
from address_book_pb2 import Person


danielle = Person()
person.id = 42
person.name = "Danielle Hanks"
person.email = "pebkac@example.com"
phone = person.phones.add()
phone.number = "(123) 456-7890"
phone.type = Person.PhoneNumber.PHONE_TYPE_MOBILE

address_book = AddressBook()
address_book.people.append(danielle)
address_book.SerializeToString()

with open("data/address_book.bin", "rb") as fin:
  data = fin.read()

imported_address_book = AddressBook.FromString(data)
