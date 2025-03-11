from .IDocumentRepository import IDocumentRepository
import yaml
import markdown

class DocumentRepository(IDocumentRepository):
    def __init__(self):
        self._yamlPath_string = ""
        self._markdownPath_string = ""
        self._yamlData_dict = {}
        self._markdownData_string = ""

    def GetYamlPath(self):
        return self._yamlPath_string
    def SetYamlPath(self,value):
        self._yamlPath_string = value

    def GetYamlDataDict(self):
        return self._yamlData_dict
    def SetYamlDataDict(self,value):
        self._yamlData_dict = value

    def GetMarkdownPath(self):
        return self._markdownPath_string
    def SetMarkdownPath(self,value):
        self._markdownPath_string = value

    def GetMarkdownDataStr(self):
        return self._markdownData_string
    def SetMarkdownDataStr(self,value):
        self._markdownData_string = value

    def ReadYaml(self) -> dict:
        with open(self._yamlPath_string, 'r') as file:
            return yaml.safe_load(file)

    def WriteYaml(self):
        with open(self._yamlPath_string, 'w') as file:
            yaml.safe_dump(self._yamlData_dict, file)

    def ReadMarkdown(self) -> str:
        with open(self._markdownPath_string, 'r') as file:
            return file.read()

    def WriteMarkdown(self):
        with open(self._markdownPath_string, 'w') as file:
            file.write(markdown.markdown(self._markdownData_string))
