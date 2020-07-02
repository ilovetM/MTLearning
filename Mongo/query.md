```js
# 查找上传了upload的真实用户数数目
db.getCollection('upload').distinct("LCID", {result:0, "LCID": /^(?!D).*$/})

# 查找真实用户数数目
db.getCollection('proj.info').distinct("LCID", {"LCID": /^(?!Demo|DEMO|demo|TEST).*$/})
```