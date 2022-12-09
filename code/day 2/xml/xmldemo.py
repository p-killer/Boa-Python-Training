import xml.dom.minidom

def main():
    '''use the parse() function to load and parse
    xml file'''
    doc=xml.dom.minidom.parse("mydata.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    #get a list of XML tags from doc and print each
    expert=doc.getElementsByTagName('expert')
    print("expertise in %d skills:" % expert.length)
    for skill in expert:
        print(skill.getAttribute("name"))

    newskill=doc.createElement("expert")
    newskill.setAttribute("name","BigData")
    doc.firstChild.appendChild(newskill)
    print("New element is added")

    expert = doc.getElementsByTagName('expert')
    print("expertise in %d skills:" % expert.length)
    for skill in expert:
        print(skill.getAttribute("name"))

if __name__ == '__main__':
    main()
