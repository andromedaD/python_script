# from xml.dom import minidom
#
# dom=minidom.parse('Class_info.xml')
#
# root=dom.documentElement
#
# tags=root.getElementsByTagName('student')
#
# print(tags[0].nodeName)
# print(tags[0].nodeType)
# print(tags[0].nodeValue)
# print(tags[0].tx`agName)
#
# from xml.dom import minidom
# dom=minidom.parse('Class_info.xml')
#
# root=dom.documentElement
#
# tags=root.getElementsByTagName('student')
#
# print(tags[0].nodeName)
# print(tags[0].nodeValue)
# print(tags[0].nodeType)
#


# from xml.dom import minidom
# dom = minidom.parse('Class_info.xml')
#
# root=dom.documentElement
#
# tags=root.getElementsByTagName('student')
#
# print(tags[0].nodeName)
# print(tags[0].nodeValue)
# print(tags[0].nodeType)
#


from xml.dom import minidom

dom=minidom.parse('Class_info.xml')
root=dom.documentElement

tags=root.getElementsByTagName('student')

print(tags[0].nodeName)
print(tags[0].nodeValue)
print(tags[0].nodeType)

