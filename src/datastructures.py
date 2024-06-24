
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = "Jackson"
        self._next_id = 4
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "last_name": last_name
            },
            {
                "id":2,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3],
                "last_name": last_name

            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1],
                "last_name": last_name


            }
        ]

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método
        ## Agrega un nuevo miembro a la lista de _members
        # member["id"] = self._generate_id()
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y elimina el miembro con el id proporcionado
        self._members = [member for member in self._members if member["id"] != id]
        return self._members

    def get_member(self, id):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                return member
        return None
            
    def get_all_members(self):
        return self._members