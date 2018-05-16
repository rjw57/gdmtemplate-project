"""Unit tests for `university_media.py`"""

import copy
import unittest
import automationproject


class Context:
    def __init__(self, env, properties):
        self.env = env
        self.properties = properties


class UniversityMediaTestCase(unittest.TestCase):
    """Tests for `project.py`."""
    default_env = {
        'name': 'pi-dash',
        'project_number': '1234',
        'current_time': 0
    }

    default_properties = {
        'project-id': 'some-project',
        'project-name': 'Some project name',
        'parent-folder-id': "1234",
        'billing-account-name': 'foo',
    }

    def test_patch_iam_policy_with_owner(self):
        """Test that we set the right values for project owners"""
        env = copy.deepcopy(self.default_env)
        properties = copy.deepcopy(self.default_properties)
        context = Context(env, properties)
        resources = automationproject.GenerateConfig(context)['resources']

        expected_add_patch = [{
            'role': 'roles/owner',
            'members': automationproject.ADMINS,
        }]
        self.assertEquals(
            expected_add_patch, resources[0]['properties']['iam-policy-patch']['add'])
