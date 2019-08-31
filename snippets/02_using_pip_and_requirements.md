**Install a package using pip**
```
pip install SomePackage            # latest version
pip install SomePackage==1.0.4     # specific version
pip install 'SomePackage>=1.0.4'   # minimum version
```
Unistall package
```
pip uninstall SomePackage
```
**Search for package**
```
pip search "query"
```
**Add packages to requirements.txt**
```
pip freeze > requirements.txt
```
**Install package from requirements.txt file**
```
pip install -r requirements.txt
```
**Use a proxy with pip install**
```
pip install <package_name> --proxy http://www-proxy
```
