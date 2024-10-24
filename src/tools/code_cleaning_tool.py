import re
from crewai_tools import BaseTool


class CodeCleaningTool(BaseTool):
    name = "Code Cleaning Tool"
    description = "Useful for cleaning code snippets"

    def _run(self, text: str) -> str:
        """
        Extracts text between ``` and ``` using regex.
        Returns the first matching code block found.
        
        Args:
            text (str): Input string containing code block with ``` markers
            
        Returns:
            str: Extracted text between markers, or empty string if no match
        """
        pattern = r'```(.*?)```'
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ''