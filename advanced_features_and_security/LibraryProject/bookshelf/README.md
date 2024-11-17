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


# Security Configuration Documentation

## Security Settings
- DEBUG=False: Disables detailed error messages in production for security.
- SECURE_BROWSER_XSS_FILTER: Enables X-XSS-Protection header.
- X_FRAME_OPTIONS='DENY': Prevents the site from being embedded in iframes.
- SECURE_CONTENT_TYPE_NOSNIFF: Prevents the browser from guessing content types.
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE: Ensures cookies are sent only over HTTPS.

## CSRF Protection
- Added {% csrf_token %} in all forms.

## ORM Usage for SQL Injection Protection
- Used Django ORM to prevent SQL injection, ensuring all queries are parameterized.

## Content Security Policy (CSP)
- Configured CSP header to restrict content sources, reducing XSS risks.