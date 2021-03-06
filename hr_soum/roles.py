from rolepermissions.roles import AbstractUserRole

class SuperAdmin(AbstractUserRole):
   available_permissions = {
       'view_user': True,
       'delete_user': True
   }

class Administrateur(AbstractUserRole):
   available_permissions = {
       'create_employer': True,
        'create_department': True,
        'create_position': True,
        'affect_to_department': True,
        'affect_to_position': True,
        'make_user_a_manager': True,
        'request_leave': True,
        'approuve_all_leave': True,
        'reject_all_leave': True,
        'manage_leave_settings': True,
        'view_all_leave_history': True,
   }
class HR(AbstractUserRole):
    available_permissions = {
        'create_employer': True,
        'view_employer': True,
        'create_department': True,
        'view_department': True,
        'view_function': True,
        'create_position': True,
        'affect_to_department': True,
        'affect_to_position': True,
        'make_user_a_manager': True,
        'request_leave': True,
        'approuve_all_leave': True,
        'reject_all_leave': True,
        'manage_leave_settings': True,
        'view_all_leave_history': True,
    }

class Manager(AbstractUserRole):
    available_permissions = {
        'request_leave': True,
        'approuve_leave': True,
        'reject_leave': True,
        'view_leave_history': True,
    }

class Employer(AbstractUserRole):
    available_permissions = {
        'request_leave': True,
    }