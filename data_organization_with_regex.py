import re

text = "<url>https://xcd32112.smart_meter.com</url>"

pattern = "(<url>https:\/\/)(?P<title>.*)(<\/url>)"

for item in re.finditer(pattern,text,re.VERBOSE):
    print(item.groupdict())
