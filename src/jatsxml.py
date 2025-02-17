import subprocess
import xml.etree.ElementTree as ET

# this function takes the best parts of two jats files and glues them together
def get_xml():
    # Step 1: Run the latex-to-jats conversion
    run_latexmlc()

    # Step 2: combine the mainly-header jats file with the mainly-body-and-footer jats file
    front_xml = templates.get_template("jats.xml").render(locals())
    merged_xml = merge_jats(front_xml, "pinda.xml")

    # Step 3: post-process a bit
    final_xml = comment_first_paragraph(merged_xml)

    # I expect a little more post-processing :)
    return final_xml

def run_latexmlc():
    """Runs latexmlc and generates a JATS XML file."""
    command = ["latexmlc", "--destination=pinda.xml", "--format=jats", "main"] #another name is possible, too
    subprocess.run(command, check=True)

def merge_jats(front_xml, body_xml):
    """Merge two JATS XML files: front + body."""
    front_tree = ET.ElementTree(ET.fromstring(front_xml))
    body_tree = ET.ElementTree(ET.parse("pinda.xml"))

    front_root = front_tree.getroot()
    body_root = body_tree.getroot()

    for section in ["body", "back"]:
        section_element = body_root.find(section)
        if section_element is not None:
            front_root.append(section_element)

    return ET.tostring(front_root, encoding="unicode")

def comment_first_paragraph(jats_xml):
    """Find the first <p> in <body> and comment it out."""
    tree = ET.ElementTree(ET.fromstring(jats_xml))
    body = tree.find("body")

    if body is not None:
        first_p = body.find("p")
        if first_p is not None:
            comment = ET.Comment(ET.tostring(first_p, encoding="unicode"))
            body.remove(first_p)
            body.insert(0, comment)

    return ET.tostring(tree.getroot(), encoding="unicode")
