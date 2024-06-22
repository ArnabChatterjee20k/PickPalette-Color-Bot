from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains.sequential import SimpleSequentialChain
from services.templates import template_for_multiple_palettes , template_single_best_palette ,template_single_best_palette_color_theory,template_for_multiple_palettes_color_theory

model = "gemini-pro"
class AI:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model=model)

    def _generate_multiple_palette_chain(self,description,app_descpriptions):
        template = template_for_multiple_palettes_color_theory

        prompt = PromptTemplate.from_template(template=template)

        parser = JsonOutputParser()
        chain = prompt | self.model | parser
        return chain.invoke({"description":description,"info":app_descpriptions})

    def _generate_best_palette_chain(self,description,palettes):
        template = template_single_best_palette_color_theory

        prompt = PromptTemplate.from_template(template=template)

        parser = JsonOutputParser()
        chain = prompt | self.model | parser
        return chain.invoke({"description":description,"info":palettes})

    def chat(self,app_descpriptions:str,description:str):
        palettes = self._generate_multiple_palette_chain(description=description,app_descpriptions=app_descpriptions)
        palettes = palettes.get("palette")
        print(palettes)
        recommended_palette = self._generate_best_palette_chain(description=description,palettes=palettes)
        return recommended_palette