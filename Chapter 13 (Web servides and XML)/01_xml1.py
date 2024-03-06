import xml.etree.ElementTree as ET

data = """<person>
    <name>Chuck</name>
    <phone type= "intl">
        =1 734 404 3356
    </phone>
    <email hide = "yes"/>
</person>"""

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))
