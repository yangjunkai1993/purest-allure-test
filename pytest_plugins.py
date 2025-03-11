# 生成 pytest_plugins.py 文件
# cat << EOF > pytest_plugins.py

import pytest
from importlib.metadata import distributions, version

config = pytest.Config()
pm = config.pluginmanager
plugins = pm.list_name_plugin()

seen = set()
for name, plugin in plugins:
    # 跳过 pytest 内置插件
    if plugin.__class__.__module__.startswith("pytest."):
        continue
    module = plugin.__module__.split('.')[0]
    for dist in distributions():
        if any(f.split('.')[0] == module for f in dist.files):
            pkg_name = dist.metadata['Name']
            if pkg_name not in seen:
                seen.add(pkg_name)
                print(f"{pkg_name}=={version(pkg_name)}")
# EOF
