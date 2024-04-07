import yaml

def get_page(inpath=r"C:\git\ms\azure-stack-docs-pr\azure-stack\hci\guided-quick-deploy-eval.yml"):
    '''
    Get the page from the markdown file.
    '''
    try:
        with open(inpath, 'r') as f:
            page = f.read()
    except Exception as e:
        page = str(e)
    return page

page = get_page()
raw_yaml = yaml.load(page, Loader=yaml.FullLoader)
try:
    yml_metadata = raw_yaml["metadata"]
except KeyError:
    metadata = ""

print(yml_metadata)

try:
    title = yml_metadata["title"]
except KeyError:
    title = ""
try:
    meta_description = yml_metadata["description"]
except KeyError:
    meta_description = ""
try:
    author = yml_metadata["author"]
except KeyError:
    author = ""
try:
    ms_author = yml_metadata["ms.author"]
except KeyError:
    ms_author = ""
try:
    ms_service = yml_metadata["ms.service"]
except KeyError:
    ms_service = ""
try:
    ms_topic = yml_metadata["ms.topic"]
except KeyError:
    ms_topic = ""
try:
    ms_date = yml_metadata["ms.date"]
except KeyError:
    ms_date = ""

print(ms_author)