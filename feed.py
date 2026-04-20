import yaml
import xml.etree.ElementTree as xml_tree

with open('example.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss')

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('sample.xml', encoding='UTF-8', xml_declaration=True)


