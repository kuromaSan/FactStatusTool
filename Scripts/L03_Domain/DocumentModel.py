from .Function.IDocumentPolicy import IDocumentPolicy
from .Variable.DocumentConfig import DocumentConfig

class DocumnetModel():
    def __init__(self,documentPolicy:IDocumentPolicy,documentConfig:DocumentConfig):
        self.__documentPolicy = documentPolicy
        self.__documentConfig = documentConfig

    # yamlファイルをMarkdownファイルたちに書き込む
    def WriteYamlToMarkdown(self):
        pass
    
    # Markdownファイルたちをyamlファイルに書き込む
    def WriteMarkdownToYaml(self):
        pass

    # ValuationTableのOKの数を取得する
    def CountOKStatus(self):
        pass

    # ValuationTableのNGの数を取得する
    def CountNGStatus(self):
        pass
    
    # 完了していないタスクを取得する
    def findTodoTask(self):
        pass

