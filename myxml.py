import xml.etree.ElementTree as ET
import xml
data ='''
<person>
<name>Chuck</name>
<phone type="innit">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('ATTR:', tree.find('email').get('hide'))