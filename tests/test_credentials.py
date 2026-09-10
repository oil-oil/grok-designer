import importlib.machinery
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
path=Path(__file__).parents[1]/'scripts/grok-designer'
loader=importlib.machinery.SourceFileLoader('designer_test',str(path))
spec=importlib.util.spec_from_loader(loader.name,loader)
module=importlib.util.module_from_spec(spec);loader.exec_module(module)
class CredentialTests(unittest.TestCase):
    def test_environment_does_not_read_or_create_key_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'key'
            with patch.dict(os.environ,{'ZENMUX_API_KEY':'fake-test-key'}):
                self.assertEqual(module.read_api_key({'api_key_file':str(path)})[1],'fake-test-key')
            self.assertFalse(path.exists())
if __name__ == '__main__':unittest.main()
