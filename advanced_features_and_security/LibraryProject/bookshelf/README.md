# Permissions and Groups Setup

## Groups and Permissions
- Viewers: Can view model instances (permission: can_view)
- Editors: Can view, create, and edit model instances (permissions: can_view, can_create, can_edit)
- Admins: Full access (permissions: can_view, can_create, can_edit, can_delete)

## Views Protection
- Each view that modifies instances checks the required permissions using @permission_required.
- Users without the required permission will be denied access.

## Testing
- Test users were created for each group to verify permissions enforcement.