"""Creates Automation team project."""

# Admin users. These users will have admin rights over all resources created in the project.
ADMINS = [
    'user:amc203@cam.ac.uk',
    'user:mb2174@cam.ac.uk',
    'user:ph448@cam.ac.uk',
    'user:rjw57@cam.ac.uk',
    'user:si202@cam.ac.uk',
]

# Ex-admin users. These users will have any admin rights removed. When people leave the project,
# they should be added here.
EX_ADMINS = []

# APIS which should be enabled in the project.
APIS = [
    'compute.googleapis.com',
    'deploymentmanager.googleapis.com',
    'pubsub.googleapis.com',
    'storage-component.googleapis.com',
    'monitoring.googleapis.com',
    'logging.googleapis.com',
    'sqladmin.googleapis.com',
    'iam.googleapis.com',
    'cloudkms.googleapis.com',
    'cloudresourcemanager.googleapis.com',
]


def GenerateConfig(context):
    """Generates config."""

    iam_policy_patch = {}

    # Ensure ADMINS have correct roles.
    if len(ADMINS) > 0:
        iam_policy_patch['add'] = [{
            'role': 'roles/owner',
            'members': ADMINS,
        }]

    # Remove sensitive roles from EX_ADMINS.
    if len(EX_ADMINS) > 0:
        iam_policy_patch['remove'] = [{
            'role': 'roles/owner',
            'members': EX_ADMINS,
        }]

    resources = [{
        'name': context.properties['project-id'],
        'type': 'project.py',
        'properties': {
            'project-name': context.properties['project-name'],
            'parent-folder-id': context.properties['parent-folder-id'],
            'billing-account-name': context.properties['billing-account-name'],
            'apis': APIS,
            'service-accounts': [],
            'bucket-export-settings': {
                'create-bucket': True,
            },
            'set-dm-service-account-as-owner': True,
            'iam-policy-patch': iam_policy_patch,
        },
    }]

    return {'resources': resources}
